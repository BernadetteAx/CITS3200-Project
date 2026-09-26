import json
import os
from pathlib import Path
import secrets
import socket
import subprocess
import sys
import time
from urllib.error import URLError
from urllib.request import Request, urlopen

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from .helpers import GameBrowser


def pytest_addoption(parser):
    parser.addoption('--headed', action='store_true', help='Show the Chrome windows')
    parser.addoption('--run-slow', action='store_true', help='Include the real countdown test')


def pytest_collection_modifyitems(config, items):
    if not config.getoption('--run-slow'):
        for item in items:
            if 'slow' in item.keywords:
                item.add_marker(pytest.mark.skip(reason='Use --run-slow for the real countdown'))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, 'report_' + outcome.get_result().when, outcome.get_result())


@pytest.fixture
def game_server(tmp_path, request):
    """Each test gets a real, fresh Flask/Socket.IO process and independent room data."""
    with socket.socket() as reservation:
        reservation.bind(('127.0.0.1', 0))
        port = reservation.getsockname()[1]
    base_url = f'http://127.0.0.1:{port}'
    token = secrets.token_urlsafe(24)
    env = dict(os.environ, SELENIUM_TEST_TOKEN=token, PYTHONUNBUFFERED='1')
    runner = Path(__file__).with_name('server.py')
    log_path = tmp_path / 'server.log'
    with log_path.open('w') as log:
        process = subprocess.Popen([sys.executable, str(runner), str(port)],
                                   cwd=runner.parent.parent, env=env, stdout=log, stderr=log)
        try:
            deadline = time.monotonic() + 25
            while time.monotonic() < deadline:
                if process.poll() is not None:
                    pytest.fail('Test server exited:\n' + log_path.read_text())
                try:
                    with urlopen(base_url + '/__selenium__/health', timeout=1) as response:
                        if response.status == 200:
                            break
                except (URLError, TimeoutError):
                    time.sleep(0.1)
            else:
                pytest.fail('Server did not start:\n' + log_path.read_text())

            def seed(code, scenario, **options):
                req = Request(base_url + '/__selenium__/seed',
                              data=json.dumps(dict(code=code, scenario=scenario, **options)).encode(),
                              headers={'Content-Type': 'application/json', 'X-Selenium-Token': token})
                with urlopen(req, timeout=10) as response:
                    assert json.load(response)['ok']

            yield base_url, seed
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)
            failed = any(getattr(request.node, 'report_' + stage, None) and
                         getattr(request.node, 'report_' + stage).failed for stage in ('setup', 'call'))
            if failed:
                output = Path(__file__).parent / 'artifacts' / request.node.name
                output.mkdir(parents=True, exist_ok=True)
                (output / 'server.log').write_text(log_path.read_text())


@pytest.fixture
def browser_factory(game_server, request):
    browsers = []
    def create():
        options = webdriver.ChromeOptions()
        if not request.config.getoption('--headed'):
            options.add_argument('--headless=new')
        options.add_argument('--window-size=1440,1000')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--force-prefers-reduced-motion')
        # Required only for containers running as root, not ordinary desktop runs.
        if hasattr(os, 'geteuid') and os.geteuid() == 0:
            options.add_argument('--no-sandbox')
        if os.environ.get('CHROME_BINARY'):
            options.binary_location = os.environ['CHROME_BINARY']
        options.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
        service = Service(executable_path=os.environ['CHROMEDRIVER']) if os.environ.get('CHROMEDRIVER') else Service()
        driver = webdriver.Chrome(options=options, service=service)
        driver.set_page_load_timeout(30)
        browser = GameBrowser(driver, game_server[0])
        browsers.append(browser)
        return browser
    yield create
    failed = any(getattr(request.node, 'report_' + stage, None) and
                 getattr(request.node, 'report_' + stage).failed for stage in ('setup', 'call'))
    artifact_dir = Path(__file__).parent / 'artifacts' / request.node.name
    for index, browser in enumerate(browsers):
        try:
            if failed:
                artifact_dir.mkdir(parents=True, exist_ok=True)
                browser.driver.save_screenshot(str(artifact_dir / f'player-{index}.png'))
                (artifact_dir / f'player-{index}.html').write_text(browser.driver.page_source)
                (artifact_dir / f'player-{index}.json').write_text(json.dumps(browser.driver.get_log('browser'), indent=2))
        finally:
            browser.driver.quit()


@pytest.fixture
def pair(browser_factory):
    host, guest = browser_factory(), browser_factory()
    code = host.host('Abbey')
    guest.join('Alex', code)
    for browser in (host, guest):
        browser.players(2)
    return host, guest, code


@pytest.fixture
def mission_pair(pair, game_server):
    host, guest, code = pair
    game_server[1](code, 'mission')
    for browser in (host, guest):
        browser.open('/mission')
        browser.mission_challenge(1)
    return host, guest


@pytest.fixture
def auction_pair(pair, game_server):
    host, guest, code = pair
    game_server[1](code, 'auction')
    for browser in (host, guest):
        browser.open('/auction')
        browser.round(1)
    return host, guest

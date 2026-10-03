from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def test_blank_name_cannot_host(browser_factory):
    browser = browser_factory()
    browser.open('/join')
    browser.click('#hostGameBtn')
    browser.visible('#name-error-popup')
    browser.path('/join')


def test_unknown_room_returns_to_join_with_error(browser_factory):
    browser = browser_factory()
    browser.open('/join')
    browser.fill('#playerName', 'Abbey')
    browser.fill('#sessionCode', 'ZZZZZZ')
    browser.click('#joinGameBtn')
    browser.path('/join')
    browser.visible('#error-popup')
    assert browser.driver.execute_script("return sessionStorage.getItem('sessionCode')") is None


def test_players_and_readiness_sync_and_only_host_can_start(pair):
    host, guest, code = pair
    for browser in (host, guest):
        browser.text('#roomCode', code)
        browser.contains('#playerList', 'Abbey')
        browser.contains('#playerList', 'Alex')
        assert not browser.element('#startGameBtn').is_enabled()
    host.ready()
    for browser in (host, guest):
        browser.wait(lambda d: len(d.find_elements(By.CSS_SELECTOR, '.player-tile[data-state="ready"]')) == 1)
        assert not browser.element('#startGameBtn').is_enabled()
    guest.ready()
    for browser in (host, guest):
        browser.wait(lambda d: len(d.find_elements(By.CSS_SELECTOR, '.player-tile[data-state="ready"]')) == 2)
    host.wait(lambda d: host.element('#startGameBtn').is_enabled())
    assert not guest.element('#startGameBtn').is_enabled()
    guest.click('#readyToggleBtn')
    host.wait(lambda d: not host.element('#startGameBtn').is_enabled())
    guest.ready()
    host.click('#startGameBtn')
    host.path('/start_game')
    guest.path('/start_game')


def test_refresh_keeps_player_identity_without_duplicate(pair):
    host, guest, _ = pair
    player_id = guest.driver.execute_script('return window.getPlayerId()')
    guest.driver.refresh()
    guest.players(2)
    guest.wait(lambda d: d.execute_script('return window.getPlayerId()') == player_id)
    host.players(2)
    assert len(guest.driver.find_elements(By.CSS_SELECTOR, '.player-name')) == 2
    guest.wait(EC.invisibility_of_element_located((By.ID, 'instructions-popup')))


def test_host_leaving_transfers_host_role(pair):
    host, guest, _ = pair
    host.click('#leaveLobbyBtn')
    host.path('/join')
    guest.players(1)
    guest.contains('#playerList', 'HOST')
    guest.wait(lambda d: d.execute_script("return sessionStorage.getItem('isHost')") == 'true')
    assert host.driver.execute_script("return sessionStorage.getItem('playerId')") is None
    guest.ready()
    guest.wait(lambda d: guest.element('#startGameBtn').is_enabled())

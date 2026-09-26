import pytest
from selenium.webdriver.common.by import By

TOOLS = ['Rope', 'Mirror', 'Handheld Radios', 'Ice Axes', 'Water Bottle', 'Fire Starter Kit']


def test_success_text_score_consumption_and_six_challenge_completion(mission_pair):
    host, guest = mission_pair
    for index, tool in enumerate(TOOLS, 1):
        actor = host if index % 2 else guest
        actor.mission_challenge(index)
        actor.choose(tool)
        actor.click('#useItemBtn')
        for browser in (host, guest):
            browser.feedback(True)
            browser.contains('#feedbackSub', f'You use the {tool} to clear obstacle {index}.')
            browser.contains('#hotbarLabel', f'SCORE {index * 10}')
            used = browser.driver.find_elements(By.CSS_SELECTOR, '#itemGrid .item-card[data-status="used"]')
            assert len(used) == index
            assert all(not card.is_enabled() for card in used)
        actor.click('#feedbackClose')
        if index < 6:
            for browser in (host, guest):
                browser.mission_challenge(index + 1)
    for browser in (host, guest):
        browser.results(score=60, passed=6, failed=0, completed=6)
    guest.driver.refresh()
    guest.results(score=60, passed=6, failed=0, completed=6)


def test_failure_item_immediately_ends_game_for_everyone(mission_pair):
    host, guest = mission_pair
    host.choose('Knockout Gas')
    host.click('#useItemBtn')
    for browser in (host, guest):
        browser.results(score=0, passed=0, failed=1, completed=1)
        browser.contains('#challenge-results', 'The rescue ends immediately.')


def test_unsuitable_item_then_two_skips_ends_at_three_failures(mission_pair):
    host, guest = mission_pair
    host.choose('Spoon')
    host.click('#useItemBtn')
    for index in (1, 2):
        for browser in (host, guest):
            browser.feedback(False)
            browser.contains('#hotbarLabel', 'SCORE 0')
        host.click('#feedbackClose')
        for browser in (host, guest):
            browser.mission_challenge(index + 1)
        guest.click('#continueBtn')
    for browser in (host, guest):
        browser.results(score=0, passed=0, failed=3, completed=3)


@pytest.mark.slow
def test_real_countdown_resolves_a_failure(mission_pair):
    host, guest = mission_pair
    # No clock manipulation: exercise the actual browser timer and timeout event.
    host.visible('#feedbackPopup', timeout=75)
    for browser in (host, guest):
        browser.feedback(False)
        browser.contains('#feedbackSub', 'time')
        browser.contains('#hotbarLabel', 'SCORE 0')
    host.click('#feedbackClose')
    for browser in (host, guest):
        browser.mission_challenge(2)

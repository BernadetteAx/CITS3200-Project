from selenium.webdriver.common.by import By


def test_join_to_results_through_real_generated_game(pair):
    """No seeded state: navigate all game phases with two independent browsers."""
    host, guest, _ = pair
    host.ready()
    guest.ready()
    host.click('#startGameBtn')
    for browser in (host, guest):
        browser.path('/start_game')
    host.click('#startAuctionBtn')
    for browser in (host, guest):
        browser.path('/mission_description')
        browser.wait(lambda d: browser.element('#missionTitle').text.strip() != '')
    title = host.element('#missionTitle').text
    guest.text('#missionTitle', title)
    assert not guest.element('#continueAuctionBtn').is_enabled()
    host.click('#continueAuctionBtn')
    for browser in (host, guest):
        browser.path('/auction')
        browser.round(1)
    total_rounds = int(host.element('#roundText').text.split(' OF ')[1])
    assert total_rounds > 0
    for index in range(1, total_rounds + 1):
        for browser in (host, guest):
            browser.round(index)
            browser.click('#skipBtn')
    for browser in (host, guest):
        browser.mission_challenge(1)
        assert browser.element('#missionName').text.upper() == title
        browser.contains('#itemGrid', 'no equipment')
    for index in range(1, 4):
        host.click('#continueBtn')
        if index < 3:
            for browser in (host, guest):
                browser.feedback(False)
            host.click('#feedbackClose')
            for browser in (host, guest):
                browser.mission_challenge(index + 1)
    for browser in (host, guest):
        browser.results(score=0, passed=0, failed=3, completed=3)
        browser.visible('#no-inventory-items')

from selenium.webdriver.common.by import By


def test_purchase_updates_both_budgets_and_inventories(auction_pair):
    host, guest = auction_pair
    for browser in (host, guest):
        assert not browser.element('#finishBtn').is_enabled()
    host.choose('Rope')
    host.wait(lambda d: host.element('#finishBtn').is_enabled())
    guest.contains('#voteCountText', '1 / 2')
    # A teammate's vote must not appear as the guest's personal selection.
    assert not guest.driver.find_elements(By.CSS_SELECTOR, '#itemGrid [aria-pressed="true"]')
    guest.choose('Rope')
    for browser in (host, guest):
        browser.click('#finishBtn')
    for browser in (host, guest):
        browser.text('#budgetValue', '$900')
        browser.contains('#inventoryLabel', '1/8')
        assert browser.element('#inventorySlots .filled').get_attribute('title') == 'Rope'
    # Checking the following round avoids relying on a short-lived result popup.
    for browser in (host, guest):
        browser.round(2)
        browser.text('#budgetValue', '$900')


def test_tied_votes_do_not_buy_an_item(auction_pair):
    host, guest = auction_pair
    host.choose('Rope')
    guest.choose('Mirror')
    host.click('#finishBtn')
    guest.click('#finishBtn')
    for browser in (host, guest):
        browser.round(2)
        browser.text('#budgetValue', '$1000')
        browser.contains('#inventoryLabel', '0/8')


def test_unaffordable_items_are_disabled(pair, game_server):
    host, guest, code = pair
    game_server[1](code, 'auction', budget=50)
    for browser in (host, guest):
        browser.open('/auction')
        browser.round(1)
        cards = browser.driver.find_elements(By.CSS_SELECTOR, '#itemGrid .item-tile')
        assert len(cards) == 2
        assert all(not card.is_enabled() for card in cards)
        assert not browser.element('#finishBtn').is_enabled()
        browser.click('#skipBtn')
    for browser in (host, guest):
        browser.round(2)
        browser.text('#budgetValue', '$50')
        browser.contains('#inventoryLabel', '0/8')

from urllib.parse import urlparse
from selenium.common.exceptions import (ElementClickInterceptedException,
    StaleElementReferenceException, NoSuchElementException)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GameBrowser:
    """Re-find dynamic elements on every wait; use real WebDriver clicks."""
    def __init__(self, driver, base_url):
        self.driver, self.base_url = driver, base_url

    def wait(self, condition, timeout=20):
        return WebDriverWait(self.driver, timeout, poll_frequency=0.1,
            ignored_exceptions=(StaleElementReferenceException, NoSuchElementException)).until(condition)

    def open(self, path):
        self.driver.get(self.base_url + path)

    def path(self, path):
        self.wait(lambda d: urlparse(d.current_url).path == path)

    def element(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def visible(self, selector, timeout=20):
        return self.wait(EC.visibility_of_element_located((By.CSS_SELECTOR, selector)), timeout)

    def text(self, selector, expected):
        self.wait(lambda d: self.element(selector).text == str(expected))

    def contains(self, selector, expected):
        self.wait(lambda d: expected in self.element(selector).text)

    def click(self, selector):
        def attempt(driver):
            element = self.element(selector)
            if not element.is_displayed() or not element.is_enabled():
                return False
            try:
                element.click()
                return True
            except ElementClickInterceptedException:
                return False
        self.wait(attempt)

    def fill(self, selector, value):
        field = self.wait(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
        field.clear()
        field.send_keys(value)

    def host(self, name):
        self.open('/join')
        self.fill('#playerName', name)
        self.click('#hostGameBtn')
        self.path('/lobby')
        self.players(1)
        self.close_lobby_guide()
        return self.element('#roomCode').text

    def join(self, name, code):
        self.open('/join')
        self.fill('#playerName', name)
        self.fill('#sessionCode', code)
        self.click('#joinGameBtn')
        self.path('/lobby')
        self.wait(lambda d: d.execute_script('return window.getPlayerId && window.getPlayerId()'))
        self.close_lobby_guide()

    def close_lobby_guide(self):
        self.visible('#instructions-popup')
        self.click('#closeInstructionsBtn')
        self.wait(EC.invisibility_of_element_located((By.ID, 'instructions-popup')))

    def players(self, count):
        self.wait(lambda d: len(d.find_elements(By.CSS_SELECTOR, '#playerList .player-tile')) == count)

    def ready(self):
        self.click('#readyToggleBtn')
        self.contains('#readyToggleBtn', 'READY')

    def round(self, index):
        self.wait(lambda d: self.element('#roundText').text.startswith(f'{index} OF ')
                  and self.element('#skipBtn').is_enabled())

    def choose(self, name):
        """Auction and mission cards both expose a visible .item-name label."""
        def select(driver):
            for label in driver.find_elements(By.CSS_SELECTOR, '#itemGrid .item-name'):
                if label.text == name:
                    card = label.find_element(By.XPATH, './ancestor::button[1]')
                    if card.is_displayed() and card.is_enabled():
                        try:
                            card.click()
                            return True
                        except ElementClickInterceptedException:
                            return False
            return False
        self.wait(select)

    def mission_challenge(self, index):
        self.path('/mission')
        self.text('#challengeCount', f'{index} OF 6')
        self.wait(lambda d: self.element('#continueBtn').is_enabled())
        self.wait(EC.invisibility_of_element_located((By.ID, 'missionTransition')))

    def feedback(self, success):
        self.visible('#feedbackPopup')
        self.wait(lambda d: self.element('#feedbackBox').get_attribute('data-outcome') ==
                  ('success' if success else 'fail'))

    def results(self, score, passed, failed, completed):
        self.path('/result_page')
        self.text('#result-message', "YOUR TEAM'S FINAL RESULTS")
        for selector, expected in [('#final-score', score), ('#challenges-passed', passed),
                                   ('#challenges-failed', failed), ('#challenges-completed', completed),
                                   ('#total-challenges', 6)]:
            self.text(selector, expected)

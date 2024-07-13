from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site_scooter(self, base_url):
        return self.driver.get(base_url)

    def find_element_located(self, locator, time=12):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Not found {locator}')

    def wait_page(self):
        return WebDriverWait(self.driver, 10).until(EC.url_contains(Constants.DZEN_REDIRECT_URL))


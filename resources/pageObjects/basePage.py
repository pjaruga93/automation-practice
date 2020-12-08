from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    URL = ''

    def __init__(self, context):
        self.context = context
        self.driver = context.browser  # An alias to make it quicker to access the WebDriver from pages

    def open(self):
        self.context.logger.info('Opening: ' + self.URL)
        self.driver.get(self.URL)

    def click(self, by_locator, timeout=5):
        """Performs a mouse click on the element passed to it by locator"""
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)).click()

    def get_text(self, by_locator):
        """Returns element's text if selenium can handle it well

        :return: string
        """
        return self.driver.find_element(*by_locator).text

    def get_href_attribute(self, by_locator):
        """Returns the content of "href" attribute

        :return: string
        """
        return self.driver.find_element(*by_locator).get_attribute('href')

    def wait_for_element(self, located_by, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(located_by)
        )

    def wait_for_element_to_be_not_visible(self, located_by, timeout=15):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.visibility_of_element_located(located_by)
        )

    def set_parameter_and_click(self, by_locator, param):
        """Performs a mouse click on the element passed to it by locator with parameter"""
        return self.driver.find_element("xpath", by_locator.format(param)).click()

    def set_parameter_and_get_text(self, by_locator, param):
        return self.driver.find_element("xpath", by_locator.format(param)).text

    def get_elements(self, by_locator):
        return self.driver.find_elements("xpath", by_locator)

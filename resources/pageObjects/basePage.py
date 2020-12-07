from hamcrest import assert_that, equal_to
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

    def enter_text(self, by_locator, text, timeout=5):
        self.context.logger.info(f'Enter text "{text}" in Element located by {by_locator}')
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)).send_keys(text)

    def clear_and_enter_text(self, by_locator, text, timeout=5):
        self.context.logger.info(f'Clear field and enter text "{text}" in Element located by {by_locator}')
        form_input = WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(by_locator)
        )
        form_input.clear()
        form_input.send_keys(text)

    def get_text(self, by_locator):
        """Returns element's text if selenium can handle it well

        :return: string
        """
        return self.driver.find_element(*by_locator).text

    def get_text_content(self, by_locator):
        """Returns the content of "textContent" attribute

        :return: string
        """
        return self.driver.find_element(*by_locator).get_attribute('textContent')

    def get_href_attribute(self, by_locator):
        """Returns the content of "href" attribute

        :return: string
        """
        return self.driver.find_element(*by_locator).get_attribute('href')

    def switch_to_iframe_by_name(self, name):
        self.driver.switch_to.frame(name)

    def switch_back_to_main_page(self):
        self.driver.switch_to.default_content()

    def assert_if_element_is_visible(self, element):
        assert_that(element.is_element_visible(), equal_to(True))

    def assert_that_elements_are_visible(self, locators):
        for locator in locators:
            element = self.driver.find_element(*locator)
            assert_that(
                element.is_dispalyed, equal_to(True),
                f'Element located by {locator} should be visible')

    def wait_for_element(self, located_by, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(located_by)
        )

    def wait_for_element_to_be_not_visible(self, located_by, timeout=15):
        return WebDriverWait(self.driver, timeout).until_not(
            expected_conditions.visibility_of_element_located(located_by)
        )

    def wait_for_element_to_be_clickable(self, located_by, timeout=7):
        self.context.logger.info(f"Waiting {timeout}s for an element {located_by} to be clickable")
        WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(located_by),
            f'Expected to be able to click on element {located_by}'
        )

import os

from resources.locators.homePageLocators import Locators

from resources.pageObjects.basePage import BasePage


class HomePage(BasePage):
    URL = os.getenv('E2E_URL', 'http://automationpractice.com/index.php')

    def __init__(self, context):
        super().__init__(context)

    def navigate_to_wmns_product(self):
        self.click(Locators.HP_WMNS_SECTION)

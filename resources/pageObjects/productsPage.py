from resources.locators.productsPageLocators import Locators
from resources.utilities.logger import Logger

from resources.pageObjects.basePage import BasePage


class ProductsPage(BasePage, Logger):
    URL = ''

    def __init__(self, context):
        super().__init__(context)
        self.logger = context.logger

    def select_products_size(self, size):
        self.wait_for_element(Locators.COLOR_FILTERS_HEADING, 10)
        self.set_parameter_and_click(Locators.SIZE_FILTER[1], size)

    def select_product_color(self, color):
        self.wait_for_element(Locators.COLOR_FILTERS_HEADING, 10)
        self.set_parameter_and_click(Locators.COLOR_FILTER[1], color)

    def wait_for_list_load(self):
        try:
            self.wait_for_element_to_be_not_visible(Locators.FILTERS_LOADING_GIF)
        except TimeoutError:
            self.logger.exception("Timeout exception")

    def assert_that_products_size_is_filtered(self, size):
        nr_of_items_to_filter = self.set_parameter_and_get_text(Locators.SIZE_ITEMS_NUMBER[1], size)
        list_of_products = self.get_elements(Locators.PRODUCT_LIST[1])
        number_of_products = len(list_of_products)

        assert str(number_of_products) in nr_of_items_to_filter

    def assert_that_products_color_is_filtered(self, color):
        filtered_item_color = self.get_href_attribute(Locators.PRODUCT_COLOR_1ST)
        assert color in filtered_item_color

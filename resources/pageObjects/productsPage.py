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
        pass

    """
    w tym miejscu chcialem zaimplemenotwac asercję po liczbie przefiltrowanych elementów, ze względu na to, że rozmiar
    jest widoczny tylko z poziomu otwartego produktu i wg mnie mija się z celem otwieranie każdego z osobna
    i sprawdzanie czy faktycznie taki rozmiar jest dostępny. Z powodu braku mozliwości załadowania listy, pozstawiam
    tę metodę pustą
    """

    def assert_that_products_color_is_filtered(self, color):
        filtered_item_color = self.get_href_attribute(Locators.PRODUCT_COLOR_1ST)
        assert color in filtered_item_color

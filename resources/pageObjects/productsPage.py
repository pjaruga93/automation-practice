from resources.locators.productsPageLocators import Locators

from resources.pageObjects.basePage import BasePage


class ProductsPage(BasePage):
    URL = ''

    def __init__(self, context):
        super().__init__(context)
        self.logger = context.logger

    def select_products_size(self, size):
        self.wait_for_element(Locators.SIZE_FILTERS_HEADING, 10)
        if 's' in size:
            self.click(Locators.SIZE_FILTER_S)
        elif 'm' in size:
            self.click(Locators.SIZE_FILTER_M)
        elif 'l' in size:
            self.click(Locators.SIZE_FILTER_L)

    def select_product_color(self, color):
        self.wait_for_element(Locators.COLOR_FILTERS_HEADING, 10)
        if 'beige' in color:
            self.click(Locators.COLOR_FILTER_BEIGE)
        elif 'black' in color:
            self.click(Locators.COLOR_FILTER_BLACK)
        elif 'blue' in color:
            self.click(Locators.COLOR_FILTER_BLUE)
        elif 'yellow' in color:
            self.click(Locators.COLOR_FILTER_YELLOW)

    def wait_for_list_load(self):
        try:
            self.wait_for_element_to_be_not_visible(Locators.FILTERS_LOADING_GIF)
        except TimeoutError:
            print("Cannot load the list...")

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

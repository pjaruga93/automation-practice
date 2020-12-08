from selenium.webdriver.common.by import By


class Locators:

    ## -- Size filters
    SIZE_FILTERS_HEADING = (By.XPATH, '//span[contains(text(),"Size")]')
    SIZE_FILTER = (By.XPATH, '//a[text()="{}"]')
    SIZE_ITEMS_NUMBER = (By.XPATH, '//a[text()="{}"]//span')

    ## -- Color filters
    COLOR_FILTERS_HEADING = (By.XPATH, '//span[contains(text(),"Color")]')
    COLOR_FILTER = (By.XPATH, '//a[text()="{}"]')
    PRODUCT_COLOR_1ST = (By.ID, 'color_1')

    ## -- Other elements
    FILTERS_LOADING_GIF = (By.XPATH, '//body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/p[1]')
    PRODUCT_LIST = (By.XPATH, '//li[contains(@class, "ajax_block_product")]')
    PRODUCT_LIST_CSS = (By.CSS_SELECTOR, 'li.ajax_block_product')

from selenium.webdriver.common.by import By


class Locators:

    ## -- Size filters
    SIZE_FILTERS_HEADING = (By.XPATH, '//span[contains(text(),"Size")]')
    SIZE_FILTER_S = (By.XPATH, '//a[text()="S"]')
    SIZE_FILTER_M = (By.XPATH, '//a[text()="M"]')
    SIZE_FILTER_L = (By.XPATH, '//a[text()="L"]')

    ## -- Color filters
    COLOR_FILTERS_HEADING = (By.XPATH, '//span[contains(text(),"Color")]')
    COLOR_FILTER_BEIGE = (By.XPATH, '//a[text()="Beige"]')
    COLOR_FILTER_BLACK = (By.XPATH, '//a[text()="Black"]')
    COLOR_FILTER_BLUE = (By.XPATH, '//a[text()="Blue"]')
    COLOR_FILTER_YELLOW = (By.XPATH, '//a[text()="Yellow"]')
    PRODUCT_COLOR_1ST = (By.ID, 'color_1')

    ## -- Other elements
    FILTERS_LOADING_GIF = (By.XPATH, '//body[1]/div[1]/div[2]/div[1]/div[3]/div[2]/ul[1]/p[1]')

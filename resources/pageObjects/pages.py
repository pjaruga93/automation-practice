from resources.pageObjects import basePage, homePage, productsPage


class Pages:
    base_page = None  # type: basePage.BasePage
    home_page = None  # type: homePage.HomePage
    products_page = None  # type: productsPage.ProductsPage

    def __init__(self, context):
        self.base_page = basePage.BasePage(context)
        self.home_page = homePage.HomePage(context)
        self.products_page = productsPage.ProductsPage(context)


class PagesType:
    pages: Pages

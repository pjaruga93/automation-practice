import logging

from behave import step

from resources.pageObjects.pages import PagesType

logger = logging.getLogger('filterSizeSteps')


@step('I go to womens products view')
def step_impl(context: PagesType):
    context.pages.home_page.navigate_to_wmns_product()


@step('I filter those products by size "{size}"')
def step_impl(context: PagesType, size):
    context.pages.products_page.select_products_size(str(size))


@step('Visible products should be in "{size}" size')
def step_impl(context: PagesType, size):
    context.pages.products_page.wait_for_list_load()
    context.pages.products_page.assert_that_products_size_is_filtered(size)

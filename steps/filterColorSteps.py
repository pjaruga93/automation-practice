import logging

from behave import step

from resources.pageObjects.pages import PagesType

logger = logging.getLogger('filterColorSteps')


@step('I filter those products by color "{color}"')
def step_impl(context: PagesType, color):
    context.pages.products_page.select_product_color(color)


@step('Visible products should be in "{color}" color')
def step_impl(context: PagesType, color):
    context.pages.products_page.wait_for_list_load()
    context.pages.products_page.assert_that_products_color_is_filtered(color)

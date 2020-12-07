import logging

from behave import step

from resources.pageObjects.pages import PagesType

logger = logging.getLogger('exampleSteps')


@step('I am on automationpractice page')
def step_impl(context: PagesType):
    context.pages.home_page.open()

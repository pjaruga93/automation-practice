import datetime
import logging
import os

from selenium import webdriver

from resources.pageObjects import pages
from resources.utilities.logger import Logger

logging.basicConfig(
    filename='logs/logs-' + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M") + '.txt',
    level=logging.INFO,
    format="[%(levelname)-8s %(asctime)s] %(message)s"
)


def before_all(context):
    context.logger = Logger(context)
    context.logger.logger = logging.getLogger(__name__)


def before_scenario(context, scenario):
    context.logger.current_scenario = scenario.name
    context.logger.info('Base URL is: ' + os.getenv('E2E_URL', 'http://automationpractice.com/index.php'))
    context.browser = webdriver.Chrome(r"C:\Users\pjaru\Desktop\chromedriver.exe")
    context.browser.set_window_size(1350, 950)
    context.pages = pages.Pages(context)
    context.logger.info('Starting browser')


def before_step(context, step):
    context.logger.current_step = step.name


def after_scenario(context, scenario):
    context.logger.info('Closing browser')
    context.browser.quit()


def after_step(context, step):
    if step.status == 'failed':
        context.logger.debug('Taking screenshot of failed step')
        now = datetime.datetime.now()
        context.browser.save_screenshot(
            os.getcwd() + "/screenshots/" + now.strftime("%Y-%m-%d-%H-%M-") + context.scenario.name.replace(" ",
                                                                                                            "-") + ':' + step.name.replace(
                " ", "-") + ".png"
        )


def after_all(context):
    pass

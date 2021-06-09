import selenium.webdriver.common.by
from behave import *
from selenium import *
from tests.acceptance.pages_models.home_page import HomePage
from tests.acceptance.pages_models.base_page import BasePage
from tests.acceptance.pages_models.exchange_page import ExchangePage
from tests.acceptance.pages_models.hotel_form_page import HotelFormPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.header.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    print(f"Content expected: {content}")
    print(f"content text: {page.header.text}")
    assert page.header.text == content

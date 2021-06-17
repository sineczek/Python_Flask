from behave import *
from selenium.webdriver.common.keys import Keys

from tests.acceptance.pages_models.home_page import HomePage
from tests.acceptance.pages_models.base_page import BasePage
from tests.acceptance.pages_models.exchange_page import ExchangePage
from tests.acceptance.pages_models.hotel_form_page import HotelFormPage
from selenium.webdriver.support.ui import Select
from selenium import webdriver

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.header.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.header.text == content


@step('"(.*)" currency value is selected')
def step_impl(context, content):
    page = ExchangePage(context.driver)
    btn = page.currency
    btn.click()

    assert btn.get_attribute("value") == content


@then('"(.*)" field has value "(.*)"')
def step_impl(context, content, default_value):
    page = ExchangePage(context.driver)
    input_field = page.amount
    input_field.click()

    assert input_field.get_attribute("value") == default_value

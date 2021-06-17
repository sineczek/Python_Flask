from behave import *
from selenium.webdriver.common.keys import Keys

from tests.acceptance.locators.exchange_page import ExchangePageLocators
from tests.acceptance.pages_models.home_page import HomePage
from tests.acceptance.pages_models.base_page import BasePage
from tests.acceptance.pages_models.exchange_page import ExchangePage
from tests.acceptance.pages_models.hotel_form_page import HotelFormPage
from selenium.webdriver.support.ui import Select


use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.driver)
    links = page.navigation

    matching_links = [l for l in links if l.text == link_text]

    if len(matching_links) > 0:
        matching_links[0].click()
    else:
        raise RuntimeError()


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = ExchangePage(context.driver)
    page.currency(field_name).send_keys(content)


@when('I press the submit button')
def step_impl(context):
    page = ExchangePage(context.driver)
    page.submit.click()


@when('I can click on field with id "(.*)"')
def step_impl(context, field_id):
    page = ExchangePage(context.driver)
    fld = page.fields

    for f in fld:
        if f == field_id:
            assert f.get_attribute("name") == field_id


@step('I can insert "(.*)" in the "(.*)" field')
def step_impl(context, value, field_id):
    page = ExchangePage(context.driver)
    fld = page.fields

    for f in fld:
        if f == field_id:
            f.click()

    fld.send_keys(value)

@step('I can choose currency "(.*)"')
def step_impl(context, currency_value):
    page = ExchangePage(context.driver)
    fld = page.driver.find_elements_by_id('currency')

    if currency_value in fld:
        print(f"yupi'kay ei: {currency_value}")
    else:
        print('lypa')


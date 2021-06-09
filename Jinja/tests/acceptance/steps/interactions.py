from behave import *
from tests.acceptance.pages_models.home_page import HomePage
from tests.acceptance.pages_models.base_page import BasePage
from tests.acceptance.pages_models.exchange_page import ExchangePage
from tests.acceptance.pages_models.hotel_form_page import HotelFormPage

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

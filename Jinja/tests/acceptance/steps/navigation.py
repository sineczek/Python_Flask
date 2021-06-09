from behave import *
from selenium import webdriver
from tests.acceptance.pages_models.home_page import HomePage
from tests.acceptance.pages_models.exchange_page import ExchangePage
from tests.acceptance.pages_models.hotel_form_page import HotelFormPage

use_step_matcher('re')


@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path=r"C:\Users\micha\Desktop\!Nauka\Python\Udemy\Python_Flask_Full\Jinja\chromedriver\chromedriver.exe")
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the exchange page')
def step_impl(context):
    context.driver = webdriver.Chrome(
        executable_path=r"C:\Users\micha\Desktop\!Nauka\Python\Udemy\Python_Flask_Full\Jinja\chromedriver\chromedriver.exe")
    page = ExchangePage(context.driver)
    context.driver.get(page.url)


@then('I am on the exchange page')
def step_impl(context):
    expected_url = ExchangePage(context.driver).url
    print(f"expected_url: {expected_url}")
    print(f"context_url: {context.driver.current_url}")
    assert context.driver.current_url == expected_url


@then('I am on the hotel form page')
def step_impl(context):
    expected_url = HotelFormPage(context.driver).url
    print(f"expected_url: {expected_url}")
    print(f"context_url: {context.driver.current_url}")
    assert context.driver.current_url == expected_url

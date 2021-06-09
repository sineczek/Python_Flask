from tests.acceptance.locators.exchange_page import ExchangePageLocators
from tests.acceptance.pages_models.base_page import BasePage


class ExchangePage(BasePage):

    @property
    def url(self):
        return super(ExchangePage, self).url + '/exchange'

    @property
    def submit(self):
        return self.driver.find_element(*ExchangePageLocators.SUBMIT)

    @property
    def amount(self):
        return self.driver.find_element(*ExchangePageLocators.AMOUNT)

    @property
    def currency(self):
        return self.driver.find_element(*ExchangePageLocators.CURRENCY)


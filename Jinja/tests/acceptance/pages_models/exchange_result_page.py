from tests.acceptance.locators.exchange_results_page import ExchangeResultsPageLocators
from tests.acceptance.pages_models.base_page import BasePage


class ExchangeResultPage(BasePage):

    @property
    def flash_msg(self):
        return self.driver.find_element(*ExchangeResultsPageLocators.FLASH_MESSAGE)

    @property
    def result_text(self):
        return self.driver.find_element(*ExchangeResultsPageLocators.RESULT_TEXT)

    @property
    def flag(self):
        return self.driver.find_element(*ExchangeResultsPageLocators.FLAG)

    @property
    def unknown(self):
        return self.driver.find_element(*ExchangeResultsPageLocators.UNKNOWN)

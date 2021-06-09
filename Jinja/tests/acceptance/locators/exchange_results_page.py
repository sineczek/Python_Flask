from selenium.webdriver.common.by import By


class ExchangeResultsPageLocators:
    FLASH_MESSAGE = By.ID, 'flash_message'
    RESULT_TEXT = By.ID, 'result_text'
    FLAG = By.ID, 'flag'
    UNKNOWN = By.ID, 'unknown_currency'

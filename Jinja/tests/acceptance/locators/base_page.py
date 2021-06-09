from selenium.webdriver.common.by import By


class BasePageLocators:
    HEADER = By.TAG_NAME, 'h1'
    CONTENT = By.TAG_NAME, 'h1'
    NAV_LINKS = By.CLASS_NAME, 'nav-link'

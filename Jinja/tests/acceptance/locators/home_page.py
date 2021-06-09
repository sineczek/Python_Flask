from selenium.webdriver.common.by import By


class HomePageLocators:
    TITLE = By.TAG_NAME, 'title'
    CONTENT = By.TAG_NAME, 'h1'
    NAV_LINK_EXCHANGE = By.ID, 'exchange'
    NAV_LINK_HOTEL_FORM = By.ID, 'hotel_form'

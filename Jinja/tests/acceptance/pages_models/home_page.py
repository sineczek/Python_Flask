from tests.acceptance.locators.home_page import HomePageLocators
from tests.acceptance.pages_models.base_page import BasePage


class HomePage(BasePage):

    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def exchange(self):
        return self.driver.find_element(*HomePageLocators.NAV_LINK_EXCHANGE)



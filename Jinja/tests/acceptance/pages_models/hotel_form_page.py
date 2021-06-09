from tests.acceptance.locators.hotel_form_page import HotelFormLocators
from tests.acceptance.pages_models.base_page import BasePage


class HotelFormPage(BasePage):

    @property
    def url(self):
        return super(HotelFormPage, self).url + '/hotel_form'

    @property
    def hotel_form(self):
        return self.driver.find_element(*HomePageLocators.NAV_LINK_HOTEL_FORM)
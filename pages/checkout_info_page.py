from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from elements.container import Container
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page

class CheckoutInfoPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.checkout_info_title = Text(page, '[data-test="title"]', 'checkout_info_title')
        self.checkout_info_container = Container(page, '[class="checkout_info"]', 'checkout_info_container')
        self.checkout_first_name = Input(page, '[data-test="firstName"]', 'first_name')
        self.checkout_last_name = Input(page, '[data-test="lastName"]', 'last_name')
        self.checkout_info_zip = Input(page, '[data-test="postalCode"]', 'postal_code')
        self.checkout_cancel_button = Button(page, '[data-test="cancel"]', 'cancel_button')
        self.checkout_continue_button = Button(page, '[data-test="continue"]', 'continue_button')

        self.checkout_error_alert = Text(page, '[data-test="error"]', 'checkout_error_alert')



    def check_visible_checkout_header(self):
        self.checkout_info_title.check_visible()
        self.checkout_info_title.check_have_text('Checkout: Your Information')

    def check_visible_checkout_info_container(self):
        self.checkout_info_container.check_visible()

        self.checkout_first_name.check_visible()
        self.checkout_first_name.check_have_text('')

        self.checkout_last_name.check_visible()
        self.checkout_last_name.check_have_text('')

        self.checkout_info_zip.check_visible()
        self.checkout_info_zip.check_have_text('')


    def fill_checkout_info_form(self, first_name: str, last_name: str, zip_code: str):
        self.checkout_first_name.fill(first_name)
        self.checkout_first_name.check_have_value(first_name)

        self.checkout_last_name.fill(last_name)
        self.checkout_last_name.check_have_value(last_name)

        self.checkout_info_zip.fill(zip_code)
        self.checkout_info_zip.check_have_value(zip_code)


    def check_checkout_error_alert(self, epic_sadface):
        self.checkout_error_alert.check_visible()
        self.checkout_error_alert.check_have_text(epic_sadface)


    def click_checkout_cancel_button(self):
        self.checkout_cancel_button.click()

    def click_checkout_continue_button(self):
        self.checkout_continue_button.click()


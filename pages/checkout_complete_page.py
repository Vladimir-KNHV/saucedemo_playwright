from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from elements.image import Image
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)

        self.checkout_complete_title = Text(page, '[data-test="title"]', 'checkout_complete_title')

        self.checkout_complete_confirmation = Container(page, '[data-test="checkout-complete-container"]', 'complete_information')
        self.confirmation_image = Image(page, '[data-test="pony-express"]', 'confirmation_image')
        self.confirmation_title = Text(page, '[data-test="complete-header"]', 'confirmation_title')
        self.confirmation_description = Text(page, '[data-test="complete-text"]', 'confirmation_description')

        self.checkout_complete_back_home_button = Button(page, 'data-test="back-to-products"', 'back+home_button')

    def check_visible_checkout_complete_header(self):
        self.checkout_complete_title.check_visible()
        self.checkout_complete_title.check_have_text('Checkout: Complete!')

    def check_visible_confirmation(self):
        self.checkout_complete_confirmation.check_visible()

        self.confirmation_image.check_visible()

        self.confirmation_title.check_visible()
        self.confirmation_title.check_have_text('Thank you for your order!')

        self.confirmation_description.check_visible()
        self.confirmation_description.check_have_text(
            'Your order has been dispatched, and will arrive just as fast as the pony can get there!'
        )


    def click_back_home_button(self):
        self.checkout_complete_back_home_button.click()

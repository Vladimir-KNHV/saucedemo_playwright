from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.link import Link
from elements.text import Text
import allure

class NavbarComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.open_menu_button = Button(page, '[data-test="open-menu"]', 'open_menu')
        self.app_title = Text(page, '[class="app_logo"]', 'app_logo')
        self.cart_link = Link(page,'[data-test="shopping-cart-link"]', 'cart_link')

    @allure.step('Check visible navbar')
    def check_visible(self):
        self.app_title.check_visible()
        self.app_title.check_have_text('Swag Labs')

        self.open_menu_button.check_visible()
        self.cart_link.check_visible()

    
    def open_cart(self):
        self.cart_link.click()







from components.item_view_component import ItemViewComponent
from elements.button import Button
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect

from components.navigation.navbar_component import NavbarComponent

class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.item_view_component = ItemViewComponent(page)

        self.navbar = NavbarComponent(page)

        self.cart_title = Text(page, '[data-test="title"]', 'cart_title')
        self.cart_qty_label = Text(page, '[data-test="cart-quantity-label"]', 'cart_qty_label')
        self.cart_desc_label = Text(page,'[data-test="cart-desc-label"]', 'cart_desc_label')

        self.cart_item = Container(page, '[data-test="inventory-item"]', 'cart_item')


        self.cart_continue_shopping_button = Button(page,'[data-test="continue-shopping"]', 'continue_button')
        self.cart_checkout_button = Button(page,'[data-test="checkout"]', 'checkout_button')



    def check_visible_cart_header(self):
        self.cart_title.check_visible()
        self.cart_title.check_have_text('Your Cart')

        self.cart_qty_label.check_visible()
        self.cart_qty_label.check_have_text('QTY')

        self.cart_desc_label.check_visible()
        self.cart_desc_label.check_have_text('Description')

    def click_continue_shopping_button(self):
        self.cart_continue_shopping_button.click()

    def click_checkout_button(self):
        self.cart_checkout_button.click()

    def check_cart_empty(self):
        expect(self.cart_item).to_have_count(0)



    
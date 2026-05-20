from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from pages.base_page import BasePage
from playwright.sync_api import Page


class ItemPage(BasePage):
    def __init__(self,page: Page):
        super().__init__(page)

        self.item_view_component = ItemViewComponent(page)
        self.navbar = NavbarComponent(page)

        self.back_to_products_button = Button(page, '[data-test="back-to-products"]', 'back_to_products_button')

    def click_back_to_products_button(self):
        self.back_to_products_button.click()


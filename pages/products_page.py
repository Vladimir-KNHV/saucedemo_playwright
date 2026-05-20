from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.dropdown import Dropdown
from elements.text import Text
from enams.sort_option import SortOption

from pages.base_page import BasePage
from playwright.sync_api import Page


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.item_view_component = ItemViewComponent(page)

        self.products_title = Text(page, '[data-test="title"]', 'products_title')
        self.products_sort_dropdown = Dropdown(page,'[data-test="product-sort-container"]', 'dropdown')


    def check_visible_products_header(self):
        self.products_title.check_visible()
        self.products_title.check_have_text('Products')

        self.products_sort_dropdown.check_visible()

    def sort_products(self, option: SortOption):
        self.products_sort_dropdown.select_sort(option)








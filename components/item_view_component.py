from components.base_component import BaseComponent
from playwright.sync_api import Page

from elements.button import Button
from elements.image import Image
from elements.text import Text
from models.product_data import ProductItem
from elements.container import Container
import allure

class ItemViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.item = Container(page, '[data-test="inventory-item"]', 'item_card')
        self.title = Text(page, '[data-test="inventory-item-name"]', 'item_name')
        self.description = Text(page, '[data-test="inventory-item-desc"]', 'item_description')
        self.price = Text(page, '[data-test="inventory-item-price"]', 'item_price')
        self.image = Image(page, '[data-test="inventory-item"] > [class="inventory_item_img"]', 'item_img')
        self.add_cart_button = Button(page, 'button.btn_small', 'add_to_cart_button')

    @allure.step('Check visible item container at index "{index}"')
    def check_visible(
            self,
            index: int = 0,
            added: bool = False,
            has_image: bool = True,
            has_button: bool = True
    ):
        self.item.check_visible(index)
        self.title.check_visible(index)
        self.description.check_visible(index)
        self.price.check_visible(index)

        if has_image:
            self.image.check_visible(index)
        if has_button:
            self.add_cart_button.check_visible(index)

            if not added:
                self.add_cart_button.check_have_text('Add to cart', index)
            if added:
                self.add_cart_button.check_have_text('Remove', index)

    @allure.step('Add item to cart at index "{index}"')
    def click_add_to_cart_button(self, index: int):
        self.add_cart_button.click(index)

    @allure.step('Remove item from cart at index "{index}"')
    def click_remove_button(self, index: int):
        self.add_cart_button.click(index)

    @allure.step('Get item data for indexes "{indexes}"')
    def get_item_data(self, indexes: list[int] | None = None) -> list[ProductItem]:
        if indexes is None:
            indexes = range(self.item.count())

        return [
            ProductItem(
                name=self.title.get_text(index),
                description=self.description.get_text(index),
                price=float(
                    self.price.get_text(index).replace('$', '')
                ),
            )
            for index in indexes
        ]

    @allure.step('Get all prices')
    def get_all_prices(self) -> list[float]:
        return [float(p.replace('$', '')) for p in self.price.get_all_texts()]

    @allure.step('Get all names')
    def get_all_names(self) -> list[str]:
        return self.title.get_all_texts()

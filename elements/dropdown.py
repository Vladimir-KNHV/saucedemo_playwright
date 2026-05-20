from elements.base_element import BaseElement
from enams.sort_option import SortOption
import allure

class Dropdown(BaseElement):

    @property
    def type_of(self) -> str:
        return 'Dropdown'


    def select_sort(self, option: SortOption):
        with allure.step(f'Select {self.type_of} "{self.name}" with {option.value}'):
            locator = self.get_locator()
            locator.select_option(value=option.value)
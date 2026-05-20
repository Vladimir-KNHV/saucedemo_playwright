from elements.base_element import BaseElement
from playwright.sync_api import expect
import allure

class Input(BaseElement):

    @property
    def type_of(self) -> str:
        return 'Input'

    def fill(self, value: str):
        with allure.step(f'Fill {self.type_of} "{self.name}" to value "{value}"'):
            locator = self.get_locator()
            locator.fill(value)

    def check_have_value(self, value: str):
        with allure.step(f'Checking {self.type_of} "{self.name}" have value "{value}"'):
            locator = self.get_locator()
            expect(locator).to_have_value(value)




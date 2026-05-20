from elements.base_element import BaseElement
import allure

class Container(BaseElement):
    @property
    def type_of(self) -> str:
        return 'Container'

    def count(self) -> int:
        with allure.step(
                f'Getting count of {self.type_of} "{self.name}"'
        ):
            return self.get_locator().count()

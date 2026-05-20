from elements.base_element import BaseElement
import allure

class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return 'Text'

    def get_text(self, index: int | None = None) -> str:
        with allure.step(
                f'Getting text from {self.type_of} "{self.name}" with index {index}'
        ):
            locator = self.get_locator(index)
            return locator.inner_text()

    def get_all_texts(self) -> list[str]:
        with allure.step(
                f'Getting all texts from {self.type_of} "{self.name}"'
        ):
            return self.get_locator().all_inner_texts()

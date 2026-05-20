from playwright.sync_api import Page, Locator, expect
import allure
from tools.logger import get_logger

logger = get_logger('BASE_ELEMENT')


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.locator = locator
        self.name = name

    @property
    def type_of(self) -> str:
        return 'base element'

    def get_locator(self, index: int | None = None) -> Locator:
        step = f'Getting locator "{self.locator}" with index "{index}"'
        with allure.step(step):
            logger.info(step)
            locator = self.page.locator(self.locator)

            if index is not None:
                locator = locator.nth(index)

            return locator

    def click(self, index: int | None = None):
        step = f'Clicking {self.type_of} "{self.name}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(index)
            locator.click()

    def check_visible(self, index: int | None = None):
        step =f'Checking {self.type_of} "{self.name}" is visible'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(index)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, index: int | None = None):
        step = f'Checking {self.type_of} "{self.name}" have text "{text}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(index)
            expect(locator).to_have_text(text)

    def check_have_contain_text(self, text: str, index: int | None = None):
        step = f'Checking {self.type_of} "{self.name}" have contain text "{text}"'
        with allure.step(step):
            logger.info(step)
            locator = self.get_locator(index)
            expect(locator).to_contain_text(text)






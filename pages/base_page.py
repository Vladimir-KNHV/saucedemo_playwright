from playwright.sync_api import Page, expect
from typing import Pattern
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        with allure.step(f'Opening url "{url}"'):
            self.page.goto(url)

    def check_current_url(self, expected_url: Pattern[str]):
        with allure.step(f'Checking current url matches pattern "{expected_url.pattern}"'):
            expect(self.page).to_have_url(expected_url)

    def check_url_not_contains(self, text: str):
        with allure.step(f'Check URL not contains {text}'):
            assert text not in self.page.url



    
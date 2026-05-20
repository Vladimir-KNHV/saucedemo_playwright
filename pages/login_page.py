from elements.button import Button
from elements.input import Input
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page
import allure

class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username_input = Input(page,'[data-test="username"]', 'username')
        self.password_input = Input(page,'[data-test="password"]', 'password')
        self.login_button = Button(page,'[data-test="login-button"]', 'login')
        self.login_error_alert = Text(page,'[data-test="error"]', 'login_error_alert')

    @allure.step('Fill login form with')
    def fill_login_form(self, username: str, password: str):
        self.username_input.fill(username)
        self.username_input.check_have_value(username)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    @allure.step('Check login alert')
    def check_login_error_alert(self, epic_sadface):
        self.login_error_alert.check_visible()
        self.login_error_alert.check_have_text(epic_sadface)




    


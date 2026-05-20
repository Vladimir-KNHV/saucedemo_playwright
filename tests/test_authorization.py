import allure
import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
import re
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.stories import AllureStories
from tools.allure.features import AllureFeature
from allure_commons.types import Severity
from config import settings


@pytest.mark.regression
@pytest.mark.authorization
@allure.tag(AllureTag.REGRESSION, AllureTag.AUTHORIZATION)
@allure.epic(AllureEpic.AUTHORIZATION)
@allure.feature(AllureFeature.LOGIN)
class TestAuthorization:

    @pytest.mark.parametrize('username,password,epic_sadface', [
        pytest.param('noname', 'no_password', 'Epic sadface: Username and password do not match any user in this service', id='unregistered_user'),
        pytest.param('', 'secret_sauce', 'Epic sadface: Username is required', id='empty_username_valid_passord'),
        pytest.param('standard_user', '', 'Epic sadface: Password is required', id='valid_username_empty_password'),
        pytest.param('', '', 'Epic sadface: Username is required', id='empty_username_empty_password')
    ])
    @allure.title('Login with wrong username and password')
    @allure.story(AllureStories.INVALID_LOGIN)
    @allure.severity(Severity.CRITICAL)
    def test_invalid_login(self, login_page: LoginPage, username: str, password: str, epic_sadface: str):
        login_page.visit('')
        login_page.fill_login_form(username=username, password=password)
        login_page.click_login_button()
        login_page.check_url_not_contains('/inventory.html')
        login_page.check_login_error_alert(epic_sadface=epic_sadface)

    @allure.title('Login with valid username and password')
    @allure.story(AllureStories.SUCCESSFUL_LOGIN)
    @allure.severity(Severity.BLOCKER)
    def test_successful_authorization(self, login_page: LoginPage, products_page: ProductsPage):
        login_page.visit('')
        login_page.fill_login_form(username=settings.test_user.username, password=settings.test_user.password)
        login_page.click_login_button()
        login_page.check_current_url(re.compile('.*/inventory.html'))
        products_page.check_visible_products_header()





from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_info_page import CheckoutInfoPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.item_page import ItemPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from config import settings
import allure
import pytest

from allure_commons.types import Severity

from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStories

@pytest.mark.regression
@pytest.mark.e2e
@allure.tag(AllureTag.REGRESSION, AllureTag.E2E)
@allure.epic(AllureEpic.PURCHASE)
@allure.feature(AllureFeature.CHECKOUT)


class TestE2E:
    @allure.title('Successful product purchase')
    @allure.story(AllureStories.SUCCESSFUL_PURCHASE)
    @allure.severity(Severity.BLOCKER)
    def test_e2e(
            self,
            login_page: LoginPage,
            products_page: ProductsPage,
            item_page: ItemPage,
            cart_page: CartPage,
            checkout_info_page: CheckoutInfoPage,
            checkout_overview_page: CheckoutOverviewPage,
            checkout_complete_page: CheckoutCompletePage,
    ):
        login_page.visit('')

        login_page.fill_login_form(username='standard_user', password='secret_sauce')
        login_page.click_login_button()

        products_page.check_visible_products_header()
        products_page.item_view_component.click_add_to_cart_button(index=0)
        products_page.item_view_component.check_visible(index=0, added=True)

        selected_item = products_page.item_view_component.get_item_data(indexes=[0])
        products_page.navbar.open_cart()
        cart_page.check_visible_cart_header()

        cart_page.item_view_component.check_visible(index=0, added=True, has_image=False)

        selected_item_in_cart = cart_page.item_view_component.get_item_data()

        assert selected_item == selected_item_in_cart

        cart_page.click_checkout_button()

        checkout_info_page.check_visible_checkout_header()
        checkout_info_page.check_visible_checkout_info_container()
        checkout_info_page.fill_checkout_info_form(
            first_name='sdgdg',
            last_name='dgadg',
            zip_code='5246'
        )
        checkout_info_page.click_checkout_continue_button()

        checkout_overview_page.check_visible_checkout_overview_header()
        checkout_overview_page.check_visible_summary_info()

        checkout_overview_page.item_view_component.check_visible(has_image=False, has_button=False)
        selected_item_in_checkout = checkout_overview_page.item_view_component.get_item_data()


        assert selected_item_in_cart == selected_item_in_checkout
        price = sum(checkout_overview_page.item_view_component.get_all_prices())
        total_price = checkout_overview_page.get_summary_total_price()

        assert price == total_price

        checkout_overview_page.click_finish_button()

        checkout_complete_page.check_visible_checkout_complete_header()
        checkout_complete_page.check_visible_confirmation()

    




from components.item_view_component import ItemViewComponent
from components.navigation.navbar_component import NavbarComponent
from elements.button import Button
from elements.container import Container
from elements.text import Text
from pages.base_page import BasePage
from playwright.sync_api import Page, expect


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.item_view_component = ItemViewComponent(page)
        self.navbar = NavbarComponent(page)

        self.checkout_overview_title = Text(page, '[data-test="title"]', 'checkout_overview_title')
        self.cart_qty_label = Text(page,'[data-test="cart-quantity-label"]', 'qty_label')
        self.cart_desc_label = Text(page, '[data-test="cart-desc-label"]', 'desc_label')

        self.checkout_overview_item_container = Container(page, '[data-test="inventory-item"]', 'checkout_overview_item_container')

        self.summary_info_container = Container(page, '[class="summary_info"]', 'summary_info_container')
        self.payment_label = Text(page, '[data-test="payment-info-label"]', 'payment_label')
        self.payment_info_value = Text(page, '[data-test="payment-info-value"]', 'payment_info_value')
        self.shipping_info_label = Text(page,'[data-test="shipping-info-label"]', 'shipping_info_label')
        self.shipping_info_value = Text(page, '[data-test="shipping-info-value"]', 'shipping_info_value')
        self.total_info_label = Text(page,'[data-test="total-info-label"]', 'total_info_label')
        self.total_info_value = Text(page,'[data-test="subtotal-label"]', 'total_info_value')
        self.tax_label = Text(page, '[data-test="tax-label"]', 'total_info_value')
        self.summary_total_label = Text(page, '[data-test="total-label"]', 'summary_total_label')

        self.checkout_overview_cancel_button = Button(page, '[data-test="cancel"]', 'cancel_button')
        self.checkout_overview_finish_button = Button(page, '[data-test="finish"]', 'finish_button')


    def check_visible_checkout_overview_header(self):
        self.checkout_overview_title.check_visible()
        self.checkout_overview_title.check_have_text('Checkout: Overview')
        self.cart_qty_label.check_visible()
        self.cart_qty_label.check_have_text('QTY')
        self.cart_desc_label.check_visible()
        self.cart_desc_label.check_have_text('Description')

    def check_empty_overview(self):
        expect(self.checkout_overview_item_container).to_have_count(0)

    def get_summary_total_price(self) -> float:
        return float(self.total_info_value.get_text().replace('Item total: $', ''))

    def check_visible_summary_info(self):
        self.summary_info_container.check_visible()

        self.payment_label.check_visible()
        self.payment_label.check_have_text('Payment Information:')

        self.payment_info_value.check_visible()
        self.payment_info_value.check_have_contain_text('SauceCard #')

        self.shipping_info_label.check_visible()
        self.shipping_info_label.check_have_text('Shipping Information:')

        self.shipping_info_value.check_visible()
        self.shipping_info_value.check_have_text('Free Pony Express Delivery!')

        self.total_info_label.check_visible()
        self.total_info_label.check_have_text('Price Total')

        self.total_info_value.check_visible()
        self.total_info_value.check_have_contain_text('Item total: $')

        self.tax_label.check_visible()
        self.tax_label.check_have_contain_text('Tax: $')

        self.summary_total_label.check_visible()
        self.summary_total_label.check_have_contain_text('Total: $')

    def click_cancel_button(self):
        self.checkout_overview_cancel_button.click()

    def click_finish_button(self):
        self.checkout_overview_finish_button.click()
        


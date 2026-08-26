from __future__ import annotations
from pages.base_page import BasePage

class CheckoutStepOnePage(BasePage):
    URL = "/checkout-step-one.html"

    FIRST_NAME_INPUT = "#first-name"
    LAST_NAME_INPUT = "#last-name"
    POSTAL_CODE_INPUT = "#postal-code"
    CONTINUE_BUTTON = "#continue"
    CANCEL_BUTTON = "#cancel"
    ERROR_MESSAGE = "[data-test='error']"

    def fill_info(self, first_name: str, last_name: str, postal_code: int) -> CheckoutStepOnePage:
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.LAST_NAME_INPUT, last_name)
        self.fill(self.POSTAL_CODE_INPUT, postal_code)
        return self

    def continue_to_overview(self):
        from pages.checkout_page import CheckoutStepTwoPage
        self.click(self.CONTINUE_BUTTON)
        return CheckoutStepTwoPage(self.page)

    def get_error_message(self) -> str:
        return self.text_of_element(self.ERROR_MESSAGE)

class CheckoutStepTwoPage(BasePage):
    URL = "/checkout-step-two.html"

    ITEM_NAME = ".inventory_item_name"
    SUBTOTAL_LABEL = ".summary_subtotal_label"
    TAX_LABEL = ".summary_tax_label"
    TOTAL_LABEL = ".summary_total_label"
    FINISH_BUTTON = "#finish"
    CANCEL_BUTTON = "#cancel"

    def get_item_name(self) -> list[str]:
        return self.page.locator(self.ITEM_NAME).all_inner_texts()

    def get_total(self) -> float:
        text = self.text_of_element(self.TOTAL_LABEL)
        return float(text.split("$")[-1])

    def get_sub_total(self) -> float:
        text = self.text_of_element(self.SUBTOTAL_LABEL)
        return float(text.split("$")[-1])

    def get_tax(self) -> float:
        text = self.text_of_element(self.TAX_LABEL)
        return float(text.split("$")[-1])

    def finish(self):
        from pages.checkout_page import CheckoutCompletePage
        self.click(self.FINISH_BUTTON)
        return CheckoutCompletePage(self.page)

class CheckoutCompletePage(BasePage):
    URL = "/checkout-complete.html"

    COMPLETE_HEADER = ".complete-header"
    BACK_HOME_BUTTON = "#back-to-products"

    def get_confirmation_message(self) -> str:
        return self.text_of_element(self.COMPLETE_HEADER)

    def is_order_complete(self) -> bool:
        return self.is_visible(self.COMPLETE_HEADER)
    
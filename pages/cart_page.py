from __future__ import annotations
from pages.base_page import BasePage

class CartPage(BasePage):
    URL = "/cart.html"

    CART_ITEM = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CHECKOUT_BTN = "#checkout"
    CONTINUE_SHOPPING_BTN = "#continue-shopping"
    REMOVE_BTN = "button[data-test='remove-{slug}']"

    def get_item_name(self) -> list[str]:
        return self.page.locator(self.CART_ITEM_NAME).all_inner_texts()

    def get_item_count(self) -> int:
        return self.count(self.CART_ITEM)

    def remove_item(self,product_slug:str) -> None:
        self.click(self.REMOVE_BTN.format(slug=product_slug))

    def proceed_to_checkout(self):
        from pages.checkout_page import CheckoutStepOnePage
        self.click(self.CHECKOUT_BTN)
        return CheckoutStepOnePage(self.page)
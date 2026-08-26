from __future__ import annotations

from playwright.sync_api import Page

from pages.base_page import BasePage

class InventoryPage(BasePage):
    URL= "/inventory.html"

    PAGE_TITLE = '.title'
    INVENTORY_ITEM = ".inventory_item"
    INVENTORY_ITEM_NAME = ".inventory_item_name"
    INVENTORY_ITEM_PRICE = ".inventory_item_price"
    ADD_TO_CART_BTN_TEMPLATE = "button[data-test='add-to-cart-{slug}']"
    REMOVE_BTN_TEMPLATE = "button[data-test='remove-{slug}']"
    CART_BADGE = ".shopping_cart_badge"
    CART_LINK = ".shopping_cart_link"
    SORT_DROPDOWN = ".product_sort_container"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def is_loaded(self) -> bool:
        return self.is_visible(self.PAGE_TITLE) and self.text_of_element(self.PAGE_TITLE) == "Products"

    def add_to_cart(self, product_slug:str) -> None:
        self.click(self.ADD_TO_CART_BTN_TEMPLATE.format(slug=product_slug))

    def remove_from_cart(self, product_slug:str) -> None:
        self.click(self.REMOVE_BTN_TEMPLATE.format(slug=product_slug))

    def cart_count(self) -> int:
        if self.count(self.CART_BADGE) == 0:
            return 0
        return int(self.text_of_element(self.CART_BADGE))

    def goto_cart(self):
        from pages.cart_page import CartPage
        self.click(self.CART_LINK)
        return CartPage(self.page)

    def sort(self, options_value:str) -> None:
        self.select_option(self.SORT_DROPDOWN, options_value)

    def get_product_name(self) -> list[str]:
        return self.page.locator(self.INVENTORY_ITEM_NAME).all_inner_texts()

    def get_product_price(self) -> int[float]:
        raw = self.page.locator(self.INVENTORY_ITEM_PRICE).all_inner_texts()
        return [float(p.replace("$", "")) for p in raw]
    
    def logout(self) -> None:
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)
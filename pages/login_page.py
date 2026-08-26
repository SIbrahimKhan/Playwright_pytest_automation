from __future__ import annotations
from playwright.sync_api import Page
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    URL = "/"

    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MASSAGE = "[data-test='error']"
    ERROR_CLOSE_BUTTON = ".error-button"

    def __init__(self, page: Page):
        super().__init__(page)

    def load(self) -> "LoginPage":
        self.goto()
        return self

    def login(self, username:str, password:str) -> InventoryPage:
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return InventoryPage(self.page)

    def login_expect_failure(self, username:str, password:str) -> LoginPage:
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def get_error_massage(self) -> str:
        return self.text_of_element(self.ERROR_MASSAGE)

    def is_error_displayed(self) -> bool:
        return self.is_visible(self.ERROR_MASSAGE)
    
from __future__ import annotations

from playwright.sync_api import Page, expect

class BasePage:
    URL: str = ""

    def __init__(self, page: Page):
        self.page = page

    # navigation
    def goto(self, path:str = "") -> None:
        self.page.goto(path or self.URL)

    def title(self) -> str:
        return self.page.title()

    # actions
    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str) -> None:
        locator = self.page.locator(selector)
        locator.fill(value)

    def text_of_element(self, selector:str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector:str) -> bool:
        return self.page.locator(selector).is_visible()

    def count(self, selector:str) -> int:
        return self.page.locator(selector).count()

    def select_option(self, selector: str, value: str) -> None:
        self.page.locator(selector).select_option(value)

    # wait and assertions
    def wait_for_url_contains(self, fragment:str, timeout:int = 10_000) -> None:
        self.page.wait_for_url(f"**/*{fragment}*", timeout=timeout)

    def element_is_visible(self, selector:str):
        return expect(self.page.locator(selector)).to_be_visible()

    def element_has_text(self, selector:str, text:str):
        return expect(self.page.locator(selector)).to_have_text(text)
    
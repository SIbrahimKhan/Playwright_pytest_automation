import os
from pathlib import Path

import pytest
from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from utils.config import Config
from utils.test_data import USERS

SCREENSHOT_DIR = Path(__file__).resolve().parent.parent / "reports" / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser_type = getattr(playwright_instance, Config.BROWSER)
    browser = browser_type.launch(headless=Config.HEADLESS, slow_mo=Config.SLOW_MO)
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(
        base_url=Config.BASE_URL,
        viewport=Config.VIEWPORT,
    )
    context.set_default_timeout(Config.DEFAULT_TIMEOUT)
    yield context
    context.close()


@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture
def login_as(page):
    """Factory fixture: `login_as("standard")` logs in and returns InventoryPage."""

    def _login(user_key: str = "standard"):
        user = USERS[user_key]
        login_page = LoginPage(page).load()
        return login_page.login(user["username"], user["password"])

    return _login

# ---------------------------------------------------------------------------
# Screenshot-on-failure -> attach to pytest-html report
# ---------------------------------------------------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page is not None:
            screenshot_path = SCREENSHOT_DIR / f"{item.name}.png"
            try:
                page.screenshot(path=str(screenshot_path))
            except Exception:
                return

            # attach to pytest-html report if the plugin is active
            if hasattr(item.config, "_html"):
                pytest_html = item.config.pluginmanager.getplugin("html")
                extra = getattr(report, "extra", [])
                relative = os.path.relpath(screenshot_path, start=Path.cwd())
                extra.append(pytest_html.extras.image(relative))
                report.extra = extra

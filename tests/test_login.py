import pytest

from pages.login_page import LoginPage
from utils.test_data import USERS, ERROR_MESSAGES

@pytest.mark.smoke
def test_standard_user_login(page):
    login_page = LoginPage(page).load()
    inventory_page = login_page.login(**USERS["standard"])

    assert inventory_page.is_loaded()
    assert "/inventory.html" in page.url

@pytest.mark.smoke
def test_lockec_user_sees_error(page):
    login_page = LoginPage(page).load()
    login_page.login_expect_failure(**USERS["locked_out"])

    assert login_page.is_error_displayed()
    assert login_page.get_error_massage() == ERROR_MESSAGES["locked_out"]
    assert "/inventory.html" not in page.url

@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error_key",
    [
        ("", "secret_sauce", "missing_username"),
        ("standard_user", "", "missing_password"),
        ("bad_user", "wrong_pass", "invalid_credentials"),
    ],
    ids= ["missing-username", "missing-password", "bad-credentials"],
)
def test_login_validation_error(page, username, password, expected_error_key):
    login_page = LoginPage(page).load()
    login_page.login_expect_failure(username, password)

    assert login_page.is_error_displayed()
    assert login_page.get_error_massage() == ERROR_MESSAGES[expected_error_key]
    assert "/inventory.html" not in page.url

@pytest.mark.regression
def test_logout(login_as, page):
    inventory_page = login_as("standard")
    inventory_page.logout()

    assert "https://www.saucedemo.com/" in page.url

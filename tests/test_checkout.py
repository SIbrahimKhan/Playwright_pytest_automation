import pytest

from utils.test_data import *

@pytest.mark.regression
def test_checkout_positive_flow(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])
    cart_page = inventory_page.goto_cart()
    checkout_page = cart_page.proceed_to_checkout()

    step_two = checkout_page.fill_info(**CHECKOUT_INFO["valid"]).continue_to_overview()

    names = step_two.get_item_name()
    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Onesie" in names
    
    complete_page = step_two.finish()
    assert complete_page.is_order_complete()
    assert complete_page.get_confirmation_message() == "Thank you for your order!"

@pytest.mark.regression
def test_check_amount(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])
    cart_page = inventory_page.goto_cart()
    checkout_page = cart_page.proceed_to_checkout()

    step_two = checkout_page.fill_info(**CHECKOUT_INFO["valid"]).continue_to_overview()

    sub_total = step_two.get_sub_total()
    tax = checkout_page.get_tax()
    total = checkout_page.get_total()

    assert round(sub_total + tax, 2) == round(total, 2)

@pytest.mark.regression
@pytest.mark.parametrize(
    "first_name, last_name, postal_code, expected_error_key",
    [
        ('', 'joey', '599901', 'missing_first_name'),
        ('Tribbiani', '', '560032', 'missing_last_name'),
        ('Tribbiani', 'joey', '', 'missing_postal_code'),
    ],
    ids= ["missing-first-name", "missing-last-name", "missing-postal-code"],
)
def checkout_info_validation(login_as, first_name, last_name, postal_code, expected_error_key):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])
    cart_page = inventory_page.goto_cart()
    checkout_page = cart_page.proceed_to_checkout()

    checkout_page.fill_info(first_name, last_name, postal_code)
    checkout_page = cart_page.proceed_to_checkout()
    assert checkout_page.get_error_message() == ERROR_MESSAGES[expected_error_key]

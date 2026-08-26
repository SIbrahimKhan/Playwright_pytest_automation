import pytest
from utils.test_data import PRODUCTS

@pytest.mark.regression
def test_verify_added_products(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])

    cart_page = inventory_page.goto_cart()

    assert cart_page.get_item_count() == 2
    names = cart_page.get_item_name()
    assert "Sauce Labs Backpack" in names
    assert "Sauce Labs Onesie" in names

@pytest.mark.regression
def test_remove_items_from_cart(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])

    cart_page = inventory_page.goto_cart()
    cart_page.remove_item(PRODUCTS["backpack"])

    names = cart_page.get_item_name()
    assert cart_page.get_item_count() == 1
    assert "Sauce Labs Backpack" not in names

@pytest.mark.regression
def test_back_to_continue_shopping(login_as, page):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])
    
    cart_page = inventory_page.goto_cart()
    cart_page.click(cart_page.CONTINUE_SHOPPING_BTN)

    assert "/inventory.html" in page.url
    


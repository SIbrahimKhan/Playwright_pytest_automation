import pytest
from utils.test_data import PRODUCTS

@pytest.mark.regression
def test_add_product_to_cart(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["backpack"])

    assert inventory_page.cart_count() == 1

@pytest.mark.regression
def test_add_multiple_products_to_cart(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["bike_light"])
    inventory_page.add_to_cart(PRODUCTS["bolt_tshirt"])
    inventory_page.add_to_cart(PRODUCTS["onesie"])

    assert inventory_page.cart_count() == 3

@pytest.mark.regression
def test_remove_from_cart(login_as):
    inventory_page = login_as("standard")
    inventory_page.add_to_cart(PRODUCTS["red_tshirt"])
    assert inventory_page.cart_count() == 1

    inventory_page.remove_from_cart(PRODUCTS["red_tshirt"])
    assert inventory_page.cart_count() == 0

@pytest.mark.regression
@pytest.mark.parametrize(
    "sort_option, assertion",
    [
        ("az", lambda names: names == sorted(names)),
        ("za", lambda names: names == sorted(names, reverse=True)),
    ],
    ids=["name-a-to-z", "name-z-to-a"],
)
def test_sort_by_name(login_as, sort_option, assertion):
    inventory_page = login_as("standard")
    inventory_page.sort(sort_option)

    names = inventory_page.get_product_name()
    assert assertion(names)

@pytest.mark.regression
@pytest.mark.parametrize(
    "sort_option, price",
    [
        ("lohi", True), ("hilo", False)
    ],
    ids= ["price-low-to-high", "price-high-to-low"]
)
def test_sort_by_price(login_as, sort_option, price):
    inventory_page = login_as("standard")
    inventory_page.sort(sort_option)

    prices = inventory_page.get_product_price()
    assert price(prices) 
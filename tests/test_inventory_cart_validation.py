import pytest
from Pages.Login import LoginPage
from Pages.InventoryPage import InventoryPage
from Pages.CartPage import CartPage


def test_all_products_validation(page):

    # Login
    login = LoginPage(page)
    login.goto_saucedemo_web()
    login.fill_login_form("standard_user","secret_sauce")
    login.click_login_btn()

    # Inventory Page
    inventory = InventoryPage(page)

    # Capture products before adding
    inventory_products = inventory.get_all_products()

    # Add all to cart
    inventory.add_all_products_to_cart()
    page.wait_for_timeout(1000)

    # Go to cart
    inventory.go_to_cart()
    page.wait_for_timeout(2000)

    # Cart Page
    cart = CartPage(page)
    cart_products = cart.get_cart_products()
    page.wait_for_timeout(1000)

    # Validation
    assert len(inventory_products) == len(cart_products), "Product count mismatch!"

    for inv, cart_item in zip(inventory_products, cart_products):
        assert inv["title"] == cart_item["title"], f"Title mismatch: {inv['title']}"
        assert inv["desc"] == cart_item["desc"], f"Description mismatch: {inv['title']}"
        assert inv["price"] == cart_item["price"], f"Price mismatch: {inv['title']}"
import pytest
from playwright.sync_api import Page

from Pages.LoginPage import LoginPage
from Pages.InventoryPage import InventoryPage
from Pages.CartPage import CartPage

from SauceDemoUITesting.Pages.CheckoutPage import CheckoutPage


def test_random_products_added_to_cart(page: Page):

    # ---------- Login ----------
    login_page = LoginPage(page)
    login_page.goto_saucedemo_web()
    login_page.fill_login_form("standard_user", "secret_sauce")
    login_page.click_login_btn()

    # ---------- Inventory Page ----------
    inventory = InventoryPage(page)
    page.wait_for_timeout(3000)

    products, count = inventory.collect_product_details(page)
    page.wait_for_timeout(3000)

    print(f"Collected {count} products")

    # ---------- Add products to cart ----------
    for index in range(count):
        inventory.add_item_to_cart(index)
    inventory.go_to_cart()

    # ---------- Cart Validation ----------
    cart = CartPage(page)


    # initial badge count
    badge_before = cart.get_cart_count()




    products_before = cart.get_cart_products()
    i=0
    for product in products:
        assert product["name"] == products_before[i]["title"]
        assert product["description"] == products_before[i]["desc"]
        assert product["price"] == products_before[i]["price"]
        i=i+1


    cart_count_before = len(products_before)
    page.wait_for_timeout(3000)
    # UI consistency check
    assert badge_before == cart_count_before

    # remove random item
    removed = cart.cart_remove_item()
    page.wait_for_timeout(3000)

    # updated counts
    badge_after = cart.get_cart_count()
    products_after = cart.get_cart_products()
    cart_count_after = len(products_after)

    # UI consistency again
    assert badge_after == cart_count_after

    # removal validation
    if badge_before > 0:
        assert badge_after == badge_before - 1
    else:
        assert badge_after == 0

    cart.go_to_checkout()

#     ---Checkout------

    checkout= CheckoutPage(page)
    checkout.fill_the_checkout_form("Abc","Cbnits","700001")
    checkout.go_to_second_page_of_checkout()
    checkout_product=checkout.get_checkout_products()
    total_price_from_checkout=0
    i=0
    for product in checkout_product:
        assert product["title"]== products_after[i]["title"]
        assert product["desc"] == products_after[i]["desc"]
        assert product["price"] == products_after[i]["price"]
        total_price_from_checkout += float(product["price"].replace("$", ""))
        i=i+1
    showing_subtotal_price=checkout.get_subtotal_Price()
    assert total_price_from_checkout==showing_subtotal_price
    checkout.go_to_finishbtn()
    print("Test completed :)")



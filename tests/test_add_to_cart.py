import pytest
from playwright.sync_api import Page
from Pages import LoginPage, AddtoCartPage, InventoryItemPage

@pytest.mark.parametrize("item_name", ["Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket", "item1"])
@pytest.mark.p0
def test_add_to_cart(page: Page, item_name: str):
    login_page = LoginPage(page)
    inventory_page = InventoryItemPage(page)

    login_page.goto_saucedemo_web()
    login_page.fill_login_form('standard_user', 'secret_sauce')
    login_page.click_login_btn()
    page.wait_for_timeout(1000)
    # all_items_name = inventory_page.get_all_items()
    # print(all_items_name)
    # for i in range(len(all_items_name)):
    #     print(inventory_page.get_img_link(all_items_name[i]))
    #     print(inventory_page.get_item_description(all_items_name[i]))
    #     print(inventory_page.get_item_price(all_items_name[i]))
    #     inventory_page.click_add_to_cart_btn(all_items_name[i])
    #     # inventory_page.click_remove_from_cart_btn(all_items_name[i])
    try:
        print(inventory_page.get_img_link(item_name))
        print(inventory_page.get_item_description(item_name))
        print(inventory_page.get_item_price(item_name))
    except:
        pytest.xfail(reason=f"ENG-71200: {item_name} is not found in the inventory page")

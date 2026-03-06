import random
from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page

        self.cart_items = page.locator('[data-test="inventory-item"]')
        self.cart_badge = page.locator('[data-test="shopping-cart-badge"]')

        self.item_name = '[data-test="inventory-item-name"]'
        self.item_desc = '[data-test="inventory-item-desc"]'
        self.item_price = '[data-test="inventory-item-price"]'

        self.remove_button = 'button'

        self.checkout =page.locator('[data-test="checkout"]')


    # get all cart products
    def get_cart_products(self):

        products = []
        count = self.cart_items.count()

        for i in range(count):

            item = self.cart_items.nth(i)

            title = item.locator(self.item_name).inner_text()
            desc = item.locator(self.item_desc).inner_text()
            price = item.locator(self.item_price).inner_text()

            products.append({
                "title": title,
                "desc": desc,
                "price": price
            })

        return products


    # cart badge number
    def get_cart_count(self):

        if self.cart_badge.count() == 0:
            return 0

        return int(self.cart_badge.inner_text())


    # randomly remove product
    def cart_remove_item(self):

        total = self.cart_items.count()

        if total == 0:
            print("No items in cart to remove")
            return None

        random_index = random.randint(0, total - 1)

        print(f"Removing product at index: {random_index}")

        self.cart_items.nth(random_index).locator(self.remove_button).click()

        return random_index
    def go_to_checkout(self):
        self.checkout.click()
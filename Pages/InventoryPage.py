import random
from playwright.sync_api import Page


class InventoryPage:

    def __init__(self, page: Page):
        self.page = page

        # each product card
        self.items = page.locator(".inventory_item")

        # elements inside product card
        self.item_name = "[data-test='inventory-item-name']"
        self.item_desc = "[data-test='inventory-item-desc']"
        self.item_price = "[data-test='inventory-item-price']"

        self.add_button = "button"

        # sorting dropdown
        self.sort_dropdown = page.locator("[data-test='product-sort-container']")

        self.cart_icon = page.locator(".shopping_cart_link")


    # total inventory items
    def get_total_items(self):
        return self.items.count()


    # random sort
    def apply_random_sort(self):

        options = ["az", "za", "lohi", "hilo"]

        random_option = random.choice(options)

        self.sort_dropdown.select_option(random_option)

        print(f"Sorting applied: {random_option}")

        self.items.first.wait_for()


    # generate random N
    def generate_random_number(self):
        total = self.get_total_items()
        return random.randint(0, total)


    # get item name
    def get_item_name(self, index):
        return self.items.nth(index).locator(self.item_name).inner_text()


    # get item description
    def get_item_description(self, index):
        return self.items.nth(index).locator(self.item_desc).inner_text()


    # get item price
    def get_item_price(self, index):
        return self.items.nth(index).locator(self.item_price).inner_text()


    # add item to cart
    def add_item_to_cart(self, index):
        self.items.nth(index).locator(self.add_button).click()


    # collect product details
    def collect_product_details(self,page):

        # Step 1: random sorting
        self.apply_random_sort()
        page.wait_for_timeout(2000)

        # Step 2: generate random N
        n = self.generate_random_number()
        page.wait_for_timeout(2000)

        print(f"Collecting first {n} products")

        products = []

        # Step 3: loop through first N
        for index in range(n):

            product = {
                "name": self.get_item_name(index),
                "description": self.get_item_description(index),
                "price": self.get_item_price(index)
            }
            print(product)

            products.append(product)
        page.wait_for_timeout(2000)
        return products, n


    # go to cart
    def go_to_cart(self):
        self.cart_icon.click()
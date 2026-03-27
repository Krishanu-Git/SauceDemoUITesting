class InventoryPage:

    def __init__(self, page):
        self.page = page
        self.inventory_items = page.locator('[data-test="inventory-item"]')
        self.cart_icon = page.locator('[data-test="shopping-cart-link"]')

    def get_all_products(self):
        products = []
        count = self.inventory_items.count()

        for i in range(count):
            item = self.inventory_items.nth(i)

            title = item.locator('[data-test="inventory-item-name"]').inner_text()
            desc = item.locator('[data-test="inventory-item-desc"]').inner_text()
            price = item.locator('[data-test="inventory-item-price"]').inner_text()

            products.append({
                "title": title,
                "desc": desc,
                "price": price
            })

        return products

    def add_all_products_to_cart(self):
        add_buttons = self.page.locator("//button[text()='Add to cart']")

        while add_buttons.count() > 0:
            add_buttons.first.click()

    def go_to_cart(self):
        self.cart_icon.click()
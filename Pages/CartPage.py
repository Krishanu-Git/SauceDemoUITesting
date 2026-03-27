class CartPage:

    def __init__(self, page):
        self.page = page
        self.cart_items = page.locator('[data-test="inventory-item"]')

    def get_cart_products(self):
        products = []
        count = self.cart_items.count()

        for i in range(count):
            item = self.cart_items.nth(i)

            title = item.locator('[data-test="inventory-item-name"]').inner_text()
            desc = item.locator('[data-test="inventory-item-desc"]').inner_text()
            price = item.locator('[data-test="inventory-item-price"]').inner_text()

            products.append({
                "title": title,
                "desc": desc,
                "price": price
            })

        return products
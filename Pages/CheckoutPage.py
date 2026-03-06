from playwright.sync_api import Playwright, Page


class CheckoutPage:
    def __init__(self,page:Page):
        self.page = page
        self.first_name=page.locator('[data-test="firstName"]')
        self.last_name=page.locator('[data-test="lastName"]')
        self.postalCode=page.locator('[data-test="postalCode"]')
        self.continuebtn=page.locator('[data-test="continue"]')
        self.item_name = page.locator('[data-test="inventory-item-name"]')
        self.item_desc =page.locator('[data-test="inventory-item-desc"]')
        self.item_price = page.locator('[data-test="inventory-item-price"]')
        self.checkout_items = page.locator('[data-test="inventory-item"]')
        self.sub_total_label=page.locator('[data-test="subtotal-label"]')
        self.finishbtn=page.locator('[data-test="finish"]')

    def fill_the_checkout_form(self,first_name,last_name,postal_code):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.postalCode.fill(postal_code)


    def go_to_second_page_of_checkout(self):
        self.continuebtn.click()

    def get_checkout_products(self):

        products = []
        count = self.checkout_items.count()

        for i in range(count):

            item = self.checkout_items.nth(i)

            title = item.locator(self.item_name).inner_text()
            desc = item.locator(self.item_desc).inner_text()
            price = item.locator(self.item_price).inner_text()

            products.append({
                "title": title,
                "desc": desc,
                "price": price
            })

        return products

    def get_subtotal_Price(self):
        subtotal_label=self.sub_total_label.inner_text().replace("Item total: $","")
        return float(subtotal_label)

    def go_to_finishbtn(self):
        self.finishbtn.click()








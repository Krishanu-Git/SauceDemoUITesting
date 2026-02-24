from playwright.sync_api import Page

class AddtoCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_btn = "#add-to-cart-sauce-labs-bike-light"
        self.item_price = "//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item_label']/following-sibling::div/div"

    def click_add_to_cart_btn(self):
        self.page.click(self.add_to_cart_btn)

    def get_item_price(self):
        return self.page.locator(self.item_price).inner_text()

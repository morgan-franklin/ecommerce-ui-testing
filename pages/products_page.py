"""
Products Page Object for SauceDemo
"""

from pages.base_page import BasePage


class ProductsPage(BasePage):
    """Products page interactions"""
    
    # Locators
    PRODUCTS_TITLE = ".title"
    PRODUCT_ITEMS = ".inventory_item"
    ADD_TO_CART_BUTTON = "button[id^='add-to-cart']"
    REMOVE_FROM_CART_BUTTON = "button[id^='remove']"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    PRODUCT_NAME = ".inventory_item_name"
    PRODUCT_PRICE = ".inventory_item_price"
    
    def is_on_products_page(self) -> bool:
        """Verify we're on products page"""
        return self.is_visible(self.PRODUCTS_TITLE)
    
    def get_page_title(self) -> str:
        """Get products page title"""
        return self.get_text(self.PRODUCTS_TITLE)
    
    def get_product_count(self) -> int:
        """Get number of products displayed"""
        return self.page.locator(self.PRODUCT_ITEMS).count()
    
    def add_first_product_to_cart(self):
        """Add first product to cart"""
        self.page.locator(self.ADD_TO_CART_BUTTON).first.click()
    
    def add_product_by_name(self, product_name: str):
        """Add specific product to cart by name"""
        # Convert product name to button ID
        # "Sauce Labs Backpack" -> "add-to-cart-sauce-labs-backpack"
        button_id = f"add-to-cart-{product_name.lower().replace(' ', '-')}"
        self.page.locator(f"#{button_id}").click()
    
    def get_cart_count(self) -> str:
        """Get shopping cart badge count"""
        return self.get_text(self.SHOPPING_CART_BADGE)
    
    def go_to_cart(self):
        """Click shopping cart"""
        self.click(self.SHOPPING_CART_LINK)
    
    def is_product_added(self) -> bool:
        """Check if cart badge is visible"""
        return self.is_visible(self.SHOPPING_CART_BADGE)

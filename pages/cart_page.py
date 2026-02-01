"""
Shopping Cart Page Object for SauceDemo
"""

from pages.base_page import BasePage


class CartPage(BasePage):
    """Shopping cart page interactions"""
    
    # Locators
    CART_ITEMS = ".cart_item"
    CART_ITEM_NAME = ".inventory_item_name"
    CART_ITEM_PRICE = ".inventory_item_price"
    REMOVE_BUTTON = "button[id^='remove']"
    CONTINUE_SHOPPING = "#continue-shopping"
    CHECKOUT_BUTTON = "#checkout"
    CART_QUANTITY = ".cart_quantity"
    
    def get_cart_items_count(self) -> int:
        """Get number of items in cart"""
        return self.page.locator(self.CART_ITEMS).count()
    
    def get_item_names(self) -> list[str]:
        """Get all item names in cart"""
        return self.page.locator(self.CART_ITEM_NAME).all_inner_texts()
    
    def remove_item_by_name(self, item_name: str):
        """Remove specific item from cart"""
        # Convert item name to button ID
        # "Sauce Labs Backpack" -> "remove-sauce-labs-backpack"
        button_id = f"remove-{item_name.lower().replace(' ', '-')}"
        self.page.locator(f"#{button_id}").click()
    
    def click_checkout(self):
        """Click checkout button"""
        self.click(self.CHECKOUT_BUTTON)
    
    def click_continue_shopping(self):
        """Click continue shopping button"""
        self.click(self.CONTINUE_SHOPPING)
    
    def is_cart_empty(self) -> bool:
        """Check if cart is empty"""
        return self.get_cart_items_count() == 0

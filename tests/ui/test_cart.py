"""
Shopping Cart Tests for SauceDemo
"""

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestCart:
    """Shopping cart functionality tests"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Login and add items before each test"""
        login_page = LoginPage(page)
        products_page = ProductsPage(page)
        
        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")
        
        # Add a product for cart tests
        products_page.add_product_by_name("Sauce Labs Backpack")
        products_page.go_to_cart()
    
    @pytest.mark.smoke
    @pytest.mark.cart
    def test_view_cart_with_items(self, page):
        """Test viewing cart with items"""
        cart_page = CartPage(page)
        
        assert not cart_page.is_cart_empty(), "Cart should have items"
        assert cart_page.get_cart_items_count() == 1, "Should have 1 item"
        print("\n✓ Cart displays items correctly")
    
    @pytest.mark.cart
    def test_cart_displays_correct_product(self, page):
        """Test cart shows correct product name"""
        cart_page = CartPage(page)
        
        items = cart_page.get_item_names()
        assert "Sauce Labs Backpack" in items, "Should show Backpack"
        print(f"\n✓ Cart shows correct item: {items[0]}")
    
    @pytest.mark.cart
    def test_remove_item_from_cart(self, page):
        """Test removing item from cart page"""
        cart_page = CartPage(page)
        
        # Remove the item
        cart_page.remove_item_by_name("Sauce Labs Backpack")
        
        # Cart should be empty
        assert cart_page.is_cart_empty(), "Cart should be empty"
        print("\n✓ Item removed from cart")
    
    @pytest.mark.cart
    def test_continue_shopping_button(self, page):
        """Test continue shopping returns to products"""
        cart_page = CartPage(page)
        products_page = ProductsPage(page)
        
        cart_page.click_continue_shopping()
        
        assert products_page.is_on_products_page(), "Should return to products"
        print("\n✓ Continue shopping works")
    
    @pytest.mark.cart
    def test_checkout_button_visible(self, page):
        """Test checkout button is visible with items"""
        cart_page = CartPage(page)
        
        assert cart_page.is_visible(cart_page.CHECKOUT_BUTTON), "Checkout button should be visible"
        print("\n✓ Checkout button visible")

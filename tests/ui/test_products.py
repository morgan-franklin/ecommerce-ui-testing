"""
Products Page Tests for SauceDemo
"""

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


class TestProducts:
    """Product page functionality tests"""
    
    @pytest.fixture(autouse=True)
    def setup(self, page):
        """Login before each test"""
        login_page = LoginPage(page)
        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")
    
    @pytest.mark.smoke
    @pytest.mark.products
    def test_products_page_loads(self, page):
        """Test products page displays correctly"""
        products_page = ProductsPage(page)
        
        assert products_page.is_on_products_page(), "Should be on products page"
        assert products_page.get_page_title() == "Products", "Title should be 'Products'"
        assert products_page.get_product_count() > 0, "Should have products displayed"
        print(f"\n✓ Found {products_page.get_product_count()} products")
    
    @pytest.mark.smoke
    @pytest.mark.products
    def test_add_single_product_to_cart(self, page):
        """Test adding a single product to cart"""
        products_page = ProductsPage(page)
        
        # Add first product
        products_page.add_first_product_to_cart()
        
        # Verify cart badge appears
        assert products_page.is_product_added(), "Cart badge should be visible"
        assert products_page.get_cart_count() == "1", "Cart count should be 1"
        print("\n✓ Product added to cart successfully")
    
    @pytest.mark.products
    def test_add_multiple_products_to_cart(self, page):
        """Test adding multiple products to cart"""
        products_page = ProductsPage(page)
        
        # Add 3 products
        products_page.add_product_by_name("Sauce Labs Backpack")
        products_page.add_product_by_name("Sauce Labs Bike Light")
        products_page.add_product_by_name("Sauce Labs Bolt T-Shirt")
        
        # Verify cart count
        assert products_page.get_cart_count() == "3", "Cart count should be 3"
        print("\n✓ Added 3 products to cart")
    
    @pytest.mark.products
    def test_remove_product_from_cart(self, page):
        """Test removing product from cart on products page"""
        products_page = ProductsPage(page)
        
        # Add product
        products_page.add_first_product_to_cart()
        assert products_page.get_cart_count() == "1", "Should have 1 item"
        
        # Remove product (button changes to "Remove" after adding)
        remove_button = page.locator("button[id^='remove']").first
        remove_button.click()
        
        # Cart badge should disappear
        assert not products_page.is_product_added(), "Cart badge should be gone"
        print("\n✓ Product removed from cart")
    
    @pytest.mark.products
    def test_product_count_accuracy(self, page):
        """Test product count is accurate"""
        products_page = ProductsPage(page)
        
        count = products_page.get_product_count()
        
        # SauceDemo has 6 products
        assert count == 6, f"Expected 6 products, found {count}"
        print(f"\n✓ Correct product count: {count}")

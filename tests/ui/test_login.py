"""
Login Tests for SauceDemo
"""

import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class TestLogin:
    """Login functionality tests"""
    
    @pytest.mark.smoke
    @pytest.mark.login
    def test_successful_login(self, page):
        """Test successful login with valid credentials"""
        # Arrange
        login_page = LoginPage(page)
        products_page = ProductsPage(page)
        
        # Act
        login_page.navigate_to_login()
        login_page.login("standard_user", "secret_sauce")
        
        # Assert
        assert products_page.is_on_products_page(), "Should be on products page"
        assert products_page.get_page_title() == "Products", "Page title should be 'Products'"
        print("\n✓ Successfully logged in")
    
    @pytest.mark.login
    def test_login_with_invalid_username(self, page):
        """Test login with invalid username"""
        # Arrange
        login_page = LoginPage(page)
        
        # Act
        login_page.navigate_to_login()
        login_page.login("invalid_user", "secret_sauce")
        
        # Assert
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_text = login_page.get_error_message()
        assert "do not match" in error_text, "Should show invalid credentials error"
        print(f"\n✓ Error displayed: {error_text}")
    
    @pytest.mark.login
    def test_login_with_invalid_password(self, page):
        """Test login with invalid password"""
        # Arrange
        login_page = LoginPage(page)
        
        # Act
        login_page.navigate_to_login()
        login_page.login("standard_user", "wrong_password")
        
        # Assert
        assert login_page.is_error_displayed(), "Error message should be displayed"
        print("\n✓ Invalid password rejected")
    
    @pytest.mark.login
    def test_login_with_empty_credentials(self, page):
        """Test login with empty username and password"""
        # Arrange
        login_page = LoginPage(page)
        
        # Act
        login_page.navigate_to_login()
        login_page.login("", "")
        
        # Assert
        assert login_page.is_error_displayed(), "Error message should be displayed"
        error_text = login_page.get_error_message()
        assert "Username is required" in error_text, "Should show username required error"
        print("\n✓ Empty credentials rejected")

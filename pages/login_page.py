"""
Login Page Object for SauceDemo
"""

from pages.base_page import BasePage


class LoginPage(BasePage):
    """Login page interactions"""
    
    # Locators
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"
    
    def navigate_to_login(self):
        """Navigate to login page"""
        self.navigate(self.URL)
    
    def login(self, username: str, password: str):
        """Perform login"""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def get_error_message(self) -> str:
        """Get login error message"""
        self.wait_for_selector(self.ERROR_MESSAGE)
        return self.get_text(self.ERROR_MESSAGE)
    
    def is_error_displayed(self) -> bool:
        """Check if error message is displayed"""
        return self.is_visible(self.ERROR_MESSAGE)

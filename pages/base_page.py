"""
Base Page Object
All page objects inherit from this class
"""

from playwright.sync_api import Page, expect


class BasePage:
    """Base class for all page objects"""
    
    def __init__(self, page: Page):
        self.page = page
    
    def navigate(self, url: str):
        """Navigate to URL"""
        self.page.goto(url)
    
    def get_title(self) -> str:
        """Get page title"""
        return self.page.title()
    
    def get_url(self) -> str:
        """Get current URL"""
        return self.page.url
    
    def click(self, selector: str):
        """Click element"""
        self.page.click(selector)
    
    def fill(self, selector: str, text: str):
        """Fill input field"""
        self.page.fill(selector, text)
    
    def get_text(self, selector: str) -> str:
        """Get element text"""
        return self.page.locator(selector).inner_text()
    
    def is_visible(self, selector: str) -> bool:
        """Check if element is visible"""
        return self.page.locator(selector).is_visible()
    
    def wait_for_selector(self, selector: str, timeout: int = 5000):
        """Wait for element to appear"""
        self.page.wait_for_selector(selector, timeout=timeout)
    
    def take_screenshot(self, name: str):
        """Take screenshot"""
        self.page.screenshot(path=f"screenshots/{name}.png")
    
    def expect_url_contains(self, text: str):
        """Assert URL contains text"""
        expect(self.page).to_have_url_containing(text)
    
    def expect_visible(self, selector: str):
        """Assert element is visible"""
        expect(self.page.locator(selector)).to_be_visible()

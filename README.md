# 🎭 E-Commerce UI Test Automation Framework

Playwright-based UI test automation framework testing SauceDemo e-commerce site.

## 🎯 Project Overview

**Site Under Test:** [SauceDemo](https://www.saucedemo.com/)  
**Framework:** Python + Playwright + pytest  
**Pattern:** Page Object Model  
**Status:** In Progress - Day 1

## 🛠️ Tech Stack

- **Language:** Python 3.11
- **UI Testing:** Playwright 1.40.0
- **Test Framework:** pytest 7.4.3
- **Design Pattern:** Page Object Model (POM)
- **Reporting:** pytest-html
- **Browser:** Firefox (optimized for M1/M2 Macs)

## 📚 Project Structure
```
ecommerce-ui-testing/
├── pages/                  # Page Object Model classes
│   ├── base_page.py       # Base page with common methods
│   ├── login_page.py      # Login page interactions
│   └── products_page.py   # Products page interactions
├── tests/
│   └── ui/
│       └── test_login.py  # Login functionality tests
├── utils/                  # Helper utilities
├── reports/                # Test reports
├── screenshots/            # Test screenshots
└── pytest.ini             # pytest configuration
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- pip

### Installation
```bash
# Clone repository
git clone https://github.com/morgan-franklin/ecommerce-ui-testing.git
cd ecommerce-ui-testing

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install
```

### Running Tests
```bash
# Run all tests
pytest -v

# Run specific test file
pytest tests/ui/test_login.py -v

# Run smoke tests only
pytest -m smoke -v

# Run with slower execution (easier to watch)
pytest -v --slowmo=1000

# Run headless (no browser window)
pytest -v --headed=false

# Generate HTML report
pytest --html=reports/report.html --self-contained-html
```

## 📊 Current Test Coverage

**Total Tests:** 4  
**Passing:** 4 (100%)  
**Last Updated:** January 30, 2026

### Login Tests ✅
- ✅ Successful login with valid credentials
- ✅ Invalid username handling
- ✅ Invalid password handling
- ✅ Empty credentials validation

### Upcoming Test Coverage
- [ ] Products page tests
- [ ] Shopping cart tests
- [ ] Checkout flow tests
- [ ] Filtering and sorting
- [ ] Remove from cart

## 🎨 Page Object Model

### BasePage
Common methods used across all pages:
- `navigate(url)` - Navigate to URL
- `click(selector)` - Click element
- `fill(selector, text)` - Fill input field
- `get_text(selector)` - Get element text
- `is_visible(selector)` - Check visibility
- `take_screenshot(name)` - Capture screenshot

### LoginPage
Login page specific methods:
- `navigate_to_login()` - Go to login page
- `login(username, password)` - Perform login
- `get_error_message()` - Get error text
- `is_error_displayed()` - Check error visibility

### ProductsPage
Products page specific methods:
- `is_on_products_page()` - Verify on products page
- `get_product_count()` - Count displayed products
- `add_product_to_cart()` - Add product to cart
- `get_cart_count()` - Get cart badge count
- `go_to_cart()` - Navigate to cart

## 🔧 Configuration

### pytest.ini
- Browser: Firefox (best for M1/M2 Macs)
- Headed mode: Visible browser
- Slow motion: 500ms between actions
- Screenshots: On failure only
- Video: On failure only

### Test Markers
- `@pytest.mark.smoke` - Quick smoke tests
- `@pytest.mark.regression` - Full regression suite
- `@pytest.mark.login` - Login-specific tests
- `@pytest.mark.products` - Product-specific tests
- `@pytest.mark.checkout` - Checkout flow tests

## 📝 Test Credentials

**Valid User:**
- Username: `standard_user`
- Password: `secret_sauce`

## 🐛 Known Issues

- Chromium crashes on M1/M2 Macs (Rosetta issue) - Use Firefox instead
- Use `--browser firefox` flag if Chromium fails

## 🎓 Learning Objectives

- ✅ Playwright setup and configuration
- ✅ Page Object Model implementation
- ✅ pytest integration with Playwright
- ✅ Test organization and markers
- [ ] Fixtures and test data management
- [ ] Parallel test execution
- [ ] CI/CD integration

## 🤝 About

**Author:** Morgan Franklin  
**Purpose:** Portfolio project demonstrating UI test automation skills  
**Related Projects:**
- [SwimMeet API Testing](https://github.com/morgan-franklin/swimmeet-api-testing) - 45 automated API tests

## 📖 Resources

- [Playwright Documentation](https://playwright.dev/python/)
- [pytest Documentation](https://docs.pytest.org/)
- [SauceDemo](https://www.saucedemo.com/) - Test site

---

*Building UI automation skills with Playwright!* 🎭✨

*Started: January 30, 2026*

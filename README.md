# Playwright Pytest Automation

A Python UI test automation framework built with **Playwright** and **Pytest**, using the **Page Object Model (POM)** pattern. Tests target [saucedemo.com](https://www.saucedemo.com), covering login, inventory, cart, and checkout flows.

## Tech Stack

- **Test runner:** Pytest
- **Browser automation:** Playwright (sync API)
- **Reporting:** pytest-html + Allure
- **Parallel execution:** pytest-xdist

## Project Structure

```
Playwright_pytest_automation/
├── pages/                  # Page Object Model classes
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/                  # Test suites
│   ├── conftest.py          # Fixtures: browser, context, page, login_as
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   └── test_checkout.py
├── utils/
│   ├── config.py            # Environment-driven configuration
│   └── test_data.py         # Test users, products, checkout info, error messages
├── pytest.ini               # Pytest configuration
└── requirements.txt
```

## Prerequisites

- Python 3.9+
- pip

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SIbrahimKhan/Playwright_pytest_automation.git
cd Playwright_pytest_automation
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Playwright browsers

```bash
playwright install
```

## Configuration

Test behavior is controlled via environment variables (see `utils/config.py`):

| Variable | Default | Description |
|----------|---------|-------------|
| `BASEURL` | `https://www.saucedemo.com` | Base URL under test |
| `HEADLESS` | `true` | Run browser headless or headed |
| `BROWSER` | `chromium` | Browser engine (`chromium`, `firefox`, `webkit`) |
| `SLOW_MO` | `0` | Delay (ms) between Playwright actions, useful for debugging |
| `DEFAULT_TIMEOUT` | `10000` | Default action timeout in ms |

Example — run headed in Firefox:

```bash
HEADLESS=false BROWSER=firefox pytest
```

## Running Tests

Run the full suite:

```bash
pytest
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

Run tests by marker:

```bash
pytest -m smoke        # fast, critical-path checks
pytest -m regression   # full functional coverage
```

Run tests in parallel:

```bash
pytest -n auto
```

## Reports

Test runs automatically generate:

- **HTML report:** `reports/report.html` (self-contained, includes screenshots on failure)
- **Allure results:** `reports/allure-results/`
- **Failure screenshots:** `reports/screenshots/`

To view the Allure report:

```bash
allure serve reports/allure-results
```

## Test Coverage

- **Login** — valid/invalid credentials, locked-out user, validation messages
- **Inventory** — product listing and sorting
- **Cart** — add/remove items
- **Checkout** — checkout flow with valid customer information

## License

No license file is currently included in this repository.

## Author

**S. Ibrahim Khan**
GitHub: [@SIbrahimKhan](https://github.com/SIbrahimKhan)
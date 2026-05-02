"""
OrangeHRM Login Page - Test Suite
Author: Nagma Khan
Tools: Python, Selenium WebDriver, PyTest
Test Site: https://opensource-demo.orangehrmlive.com (public demo site)
"""

import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


# ─── CONFIGURATION ────────────────────────────────────────────────────────────

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
VALID_USERNAME = "Admin"
VALID_PASSWORD = "admin123"


# ─── FIXTURE: Setup & Teardown ────────────────────────────────────────────────

@pytest.fixture
def driver():
    """Launch Chrome browser before each test, close after."""
    options = Options()
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Uncomment to run without browser window

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    driver.get(BASE_URL)

    yield driver  # Test runs here

    driver.quit()  # Always close browser after test


# ─── HELPER ───────────────────────────────────────────────────────────────────

def enter_credentials(driver, username, password):
    """Reusable function to fill in login form."""
    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.clear()
    username_field.send_keys(username)

    password_field = driver.find_element(By.NAME, "password")
    password_field.clear()
    password_field.send_keys(password)

    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()


# ─── TEST CASES ───────────────────────────────────────────────────────────────

class TestLogin:

    def test_TC001_valid_login(self, driver):
        """
        TC001 - Valid Login
        Description : Login with correct username and password
        Expected    : User is redirected to the Dashboard
        """
        enter_credentials(driver, VALID_USERNAME, VALID_PASSWORD)

        wait = WebDriverWait(driver, 10)
        dashboard = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h6[contains(text(),'Dashboard')]")
        ))

        assert dashboard.is_displayed(), "Dashboard not visible after valid login"
        print("PASS - TC001: Valid login redirects to Dashboard")


    def test_TC002_invalid_password(self, driver):
        """
        TC002 - Invalid Password
        Description : Login with correct username but wrong password
        Expected    : Error message is displayed, login fails
        """
        enter_credentials(driver, VALID_USERNAME, "wrongpassword")

        wait = WebDriverWait(driver, 10)
        error = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
        ))

        assert "Invalid credentials" in error.text, f"Unexpected error message: {error.text}"
        print("PASS - TC002: Invalid password shows error message")


    def test_TC003_invalid_username(self, driver):
        """
        TC003 - Invalid Username
        Description : Login with wrong username and wrong password
        Expected    : Error message is displayed
        """
        enter_credentials(driver, "wronguser", "wrongpassword")

        wait = WebDriverWait(driver, 10)
        error = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
        ))

        assert error.is_displayed(), "No error shown for invalid username"
        print("PASS - TC003: Invalid username shows error message")


    def test_TC004_empty_username(self, driver):
        """
        TC004 - Empty Username Field
        Description : Submit login form with username left blank
        Expected    : Validation error shown under username field
        """
        enter_credentials(driver, "", VALID_PASSWORD)

        wait = WebDriverWait(driver, 10)
        error = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Required']")
        ))

        assert error.is_displayed(), "No 'Required' validation shown for empty username"
        print("PASS - TC004: Empty username triggers 'Required' validation")


    def test_TC005_empty_password(self, driver):
        """
        TC005 - Empty Password Field
        Description : Submit login form with password left blank
        Expected    : Validation error shown under password field
        """
        enter_credentials(driver, VALID_USERNAME, "")

        wait = WebDriverWait(driver, 10)
        error = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Required']")
        ))

        assert error.is_displayed(), "No 'Required' validation shown for empty password"
        print("PASS - TC005: Empty password triggers 'Required' validation")


    def test_TC006_both_fields_empty(self, driver):
        """
        TC006 - Both Fields Empty
        Description : Submit login form with both fields blank
        Expected    : Two 'Required' validation errors shown
        """
        enter_credentials(driver, "", "")

        wait = WebDriverWait(driver, 10)
        errors = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//span[text()='Required']")
        ))

        assert len(errors) == 2, f"Expected 2 validation errors, found {len(errors)}"
        print("PASS - TC006: Both empty fields show 'Required' validations")


    def test_TC007_forgot_password_link(self, driver):
        """
        TC007 - Forgot Password Link
        Description : Click the 'Forgot your password?' link
        Expected    : User is taken to the Reset Password page
        """
        wait = WebDriverWait(driver, 10)
        forgot_link = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(text(),'Forgot')]")
        ))
        forgot_link.click()

        reset_heading = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//h6[contains(text(),'Reset Password')]")
        ))

        assert reset_heading.is_displayed(), "Reset Password page did not load"
        print("PASS - TC007: Forgot password link navigates to Reset Password page")


    def test_TC008_page_title(self, driver):
        """
        TC008 - Page Title Check
        Description : Verify the browser tab title on the login page
        Expected    : Title contains 'OrangeHRM'
        """
        assert "OrangeHRM" in driver.title, f"Unexpected page title: {driver.title}"
        print(f"PASS - TC008: Page title is '{driver.title}'")


    def test_TC009_logo_visible(self, driver):
        """
        TC009 - Logo Visibility
        Description : Verify OrangeHRM logo is visible on login page
        Expected    : Logo image is present and displayed
        """
        wait = WebDriverWait(driver, 10)
        logo = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//img[contains(@src,'orangehrm-logo')]")
        ))

        assert logo.is_displayed(), "OrangeHRM logo is not visible"
        print("PASS - TC009: Logo is visible on login page")


    def test_TC010_case_sensitive_username(self, driver):
        """
        TC010 - Case Sensitive Username
        Description : Login with lowercase 'admin' instead of 'Admin'
        Expected    : Login fails — username is case-sensitive
        """
        enter_credentials(driver, "admin", VALID_PASSWORD)

        wait = WebDriverWait(driver, 10)
        error = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//p[contains(@class,'oxd-alert-content-text')]")
        ))

        assert error.is_displayed(), "Expected login failure for wrong case username"
        print("PASS - TC010: Login fails for lowercase 'admin' — case sensitive confirmed")

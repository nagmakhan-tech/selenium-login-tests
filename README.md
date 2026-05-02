# OrangeHRM Login Page — Selenium Test Suite

**Author:** Nagma Khan  
**Tools:** Python · Selenium WebDriver · PyTest  
**Type:** Manual-to-Automation Practice Project  

---

## 📋 What This Project Tests

Automated test suite for the **Login Page** of [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com) — a publicly available HR application used widely for QA practice.

| Test ID | Test Case | Type |
|---------|-----------|------|
| TC001 | Valid login → redirects to Dashboard | Positive |
| TC002 | Invalid password → error message shown | Negative |
| TC003 | Invalid username → error message shown | Negative |
| TC004 | Empty username → 'Required' validation | Boundary |
| TC005 | Empty password → 'Required' validation | Boundary |
| TC006 | Both fields empty → 2 validations shown | Boundary |
| TC007 | Forgot Password link → navigates correctly | Navigation |
| TC008 | Page title contains 'OrangeHRM' | UI Check |
| TC009 | Logo is visible on login page | UI Check |
| TC010 | Lowercase username fails (case-sensitive) | Negative |

---

## 🛠️ Setup & Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install ChromeDriver
Download from: https://chromedriver.chromium.org/  
Make sure it matches your Chrome browser version.

### 3. Run all tests
```bash
pytest tests/test_login.py -v
```

### 4. Run a single test
```bash
pytest tests/test_login.py::TestLogin::test_TC001_valid_login -v
```

---

## 📁 Project Structure

```
selenium_project/
│
├── tests/
│   └── test_login.py       # All 10 test cases
│
├── requirements.txt         # Python dependencies
└── README.md                # This file
```

---

## 💡 Key Concepts Demonstrated

- **Page interaction** using Selenium `By.NAME`, `By.XPATH`
- **Explicit waits** with `WebDriverWait` and `expected_conditions`
- **PyTest fixtures** for browser setup and teardown
- **Positive, negative, and boundary** test case types
- **Reusable helper functions** to avoid code duplication
- **Clear test documentation** with TC IDs, descriptions, and expected results

---

## 🌐 Test Site

This project uses the **OrangeHRM open-source demo** — a free, publicly accessible site designed for QA practice. No login credentials are sensitive.

- URL: https://opensource-demo.orangehrmlive.com
- Demo credentials: `Admin` / `admin123`
+6

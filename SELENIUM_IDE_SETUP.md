# Selenium IDE Setup and Usage Guide

This guide explains how to use Selenium IDE with your BDD project instead of Selenium WebDriver.

## 🚀 What is Selenium IDE?

Selenium IDE is a browser extension that allows you to record and playback browser interactions. It's perfect for creating automated tests without writing code.

## 📦 Installation

### 1. Install Selenium IDE Extension

**For Chrome:**
1. Go to Chrome Web Store
2. Search for "Selenium IDE"
3. Click "Add to Chrome"
4. Confirm installation

**For Firefox:**
1. Go to Firefox Add-ons
2. Search for "Selenium IDE"
3. Click "Add to Firefox"
4. Confirm installation

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

## 🎯 How to Use Selenium IDE with Your BDD Project

### Step 1: Open Selenium IDE
1. Click on the Selenium IDE extension icon in your browser
2. Click "Create a new project"
3. Name your project (e.g., "BDD_Testing")

### Step 2: Start Recording
1. Click "Record a new test in a new project"
2. Enter the base URL for the website you want to test
3. Click "Start Recording"
4. Your browser will open and start recording your actions

### Step 3: Record Your Test Steps
Navigate through the website and perform the actions you want to test:

**Example for Jumia:**
1. Navigate to https://www.jumia.com.ng
2. Click on search box
3. Type "smartphone"
4. Click search button
5. Click on a product
6. Click "Add to Cart"
7. Verify cart icon shows item count

### Step 4: Stop Recording
1. Click "Stop Recording" in Selenium IDE
2. Your test will be saved automatically

### Step 5: Export as Python/Behave
1. In Selenium IDE, go to "Export"
2. Select "Python (Behave)"
3. Copy the generated code
4. Replace the placeholder steps in your feature files

## 📝 Example Selenium IDE Commands

### Navigation Commands
```
open | https://www.jumia.com.ng
open | https://www.refactory.ug
open | https://www.shein.com
```

### Interaction Commands
```
click | id=search-input
type | id=search-input | smartphone
click | id=search-button
click | class=add-to-cart
```

### Verification Commands
```
assertElementPresent | class=search-results
assertText | class=cart-confirmation | *added to cart*
assertTitle | *Jumia*
waitForElementPresent | id=search-results
```

## 🔧 Locator Strategies

### ID Locator
```
click | id=search-button
type | id=email | user@example.com
```

### Class Name Locator
```
click | class=add-to-cart
assertElementPresent | class=search-results
```

### XPath Locator
```
click | xpath=//button[contains(text(), 'Add to Cart')]
click | xpath=//a[contains(text(), 'Login')]
```

### Link Text Locator
```
click | linkText=Sign Up
click | linkText=My Account
```

### Name Locator
```
type | name=username | john_doe
type | name=password | secret123
```

## 📋 Step-by-Step Recording Guide

### For Jumia E-commerce:
1. **Start Recording**
   - Open Selenium IDE
   - Enter base URL: `https://www.jumia.com.ng`
   - Click "Start Recording"

2. **Record Search Functionality**
   - Click on search box
   - Type "smartphone"
   - Click search button
   - Verify results appear

3. **Record Add to Cart**
   - Click on a product
   - Click "Add to Cart"
   - Verify confirmation message

4. **Record Checkout Process**
   - Click cart icon
   - Click "Proceed to Checkout"
   - Fill in delivery details

### For Refactory Academy:
1. **Start Recording**
   - Base URL: `https://www.refactory.ug`

2. **Record Course Browsing**
   - Click "Courses" section
   - Select a course category
   - Click on a specific course

3. **Record Enrollment**
   - Click "Enroll Now"
   - Fill in registration form
   - Complete payment process

### For Shein Fashion:
1. **Start Recording**
   - Base URL: `https://www.shein.com`

2. **Record Product Browsing**
   - Click "Women" category
   - Select "Dresses" subcategory
   - Filter by size/color

3. **Record Wishlist**
   - Click "Add to Wishlist"
   - Verify item added
   - View wishlist

## 🔄 Converting Selenium IDE to Behave Steps

### Example Conversion:

**Selenium IDE Command:**
```
click | id=search-button
```

**Behave Step Definition:**
```python
@when('User clicks on the search button')
def step_impl(context):
    # Record: click | id=search-button
    pass
```

**Selenium IDE Command:**
```
type | id=search-input | smartphone
```

**Behave Step Definition:**
```python
@when('User enters "{search_term}" in the search field')
def step_impl(context, search_term):
    # Record: type | id=search-input | {search_term}
    pass
```

## 🎯 Best Practices

### 1. Use Descriptive Test Names
- Name your tests clearly (e.g., "Jumia_Search_And_Add_To_Cart")
- Use descriptive step names

### 2. Add Wait Commands
- Use `waitForElementPresent` for dynamic content
- Add `pause` commands for slow-loading elements

### 3. Use Reliable Locators
- Prefer ID locators when available
- Use XPath for complex selections
- Avoid using text that might change

### 4. Add Assertions
- Always verify expected outcomes
- Use `assertElementPresent` and `assertText`
- Add multiple verification points

### 5. Organize Your Tests
- Group related tests together
- Use consistent naming conventions
- Add comments for complex steps

## 🐛 Troubleshooting

### Common Issues:

1. **Element Not Found**
   - Check if locator is correct
   - Add wait commands
   - Verify element is visible

2. **Test Fails Intermittently**
   - Add `waitForElementPresent` commands
   - Increase pause times
   - Check for dynamic content

3. **Recording Issues**
   - Refresh the page and restart recording
   - Clear browser cache
   - Try different locator strategies

## 📚 Additional Resources

- [Selenium IDE Documentation](https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started)
- [Selenium IDE Commands Reference](https://www.selenium.dev/selenium-ide/docs/en/api/commands)
- [Behave Documentation](https://behave.readthedocs.io/)

## 🎉 Next Steps

1. Install Selenium IDE extension
2. Start recording tests for each application
3. Export tests as Python/Behave format
4. Replace placeholder steps in your feature files
5. Run your BDD tests with `behave`

Happy Testing! 🚀 
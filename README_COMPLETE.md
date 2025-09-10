# BDD Testing Project - Online Applications

This project contains comprehensive Behavior Driven Development (BDD) test scenarios for six major online applications using Gherkin syntax and Selenium IDE for test automation.

## Project Overview

This project was created as part of a classroom assignment to identify and test features of online applications using BDD methodology. The project includes:

- **5 Online Applications** with comprehensive feature testing
- **Multiple scenarios** for each feature
- **Selenium IDE** automation (browser extension)
- **Gherkin syntax** for readable test scenarios

## 🎯 Applications Covered

### 1. **Jumia E-commerce Platform** (`jumia.features`)
- **8 Features** with **20+ Scenarios**
- Features: Product Search, User Registration, Shopping Cart, Checkout, Account Management, Reviews, Wishlist, Customer Support

### 2. **Instagram Social Media** (`instagram.features`)
- **8 Features** with **20+ Scenarios**
- Features: User Authentication, Photo/Video Posting, Content Discovery, Following, Liking/Commenting, Direct Messaging, Profile Management, Content Saving

### 3. **Refactory Academy Learning Platform** (`refactory_academy.features`)
- **12 Features** with **30+ Scenarios**
- Features: Course Discovery, User Registration, Course Enrollment, Learning Experience, Assignments, Progress Tracking, Community, Mentorship, Career Services, Alumni Network, Technical Support, Mobile Learning

### 4. **Shein Fashion E-commerce** (`shein.features`)
- **12 Features** with **30+ Scenarios**
- Features: Fashion Discovery, User Registration, Product Browsing, Shopping Cart, Wishlist Management, Checkout, Style Recommendations, Reviews, Order Tracking, Community, Loyalty Program, Customer Support

### 5. **Ride-Sharing Application** (`ride_sharing.features`)
- **10 Features** with **25+ Scenarios**
- Features: User Registration, Ride Booking, Driver Matching, Ride Tracking, Payment, Ride History, Preferences, Cancellation, Ride Sharing, Safety Features

## 📁 Project Structure

```
bdd/
├── features/
│   ├── jumia.features          # Jumia e-commerce scenarios
│   ├── github.features         # GitHub development platform scenarios
│   ├── refactory_academy.features  # Refactory Academy learning scenarios
│   ├── shein.features          # Shein fashion e-commerce scenarios
│   ├── safeboda.features       # SafeBoda ride-hailing scenarios
│   ├── youtube_music.features  # YouTube Music streaming scenarios
│   ├── moviebox.features       # MovieBox streaming scenarios
│   └── steps/
│       ├── steps.py            # Original step definitions
│       └── comprehensive_steps.py  # Complete step definitions
├── venv/                       # Virtual environment
├── requirements.txt            # Python dependencies
├── README_COMPLETE.md          # This file
└── readme.md                   # Original readme
```

## 🚀 Setup and Installation

### Prerequisites
- Python 3.8 or higher
- Chrome or Firefox browser
- Selenium IDE browser extension

### Installation Steps

1. **Clone or navigate to the project directory**
   ```bash
   cd bdd
   ```

2. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Selenium IDE Extension**
   - Chrome: Go to Chrome Web Store and search for "Selenium IDE"
   - Firefox: Go to Firefox Add-ons and search for "Selenium IDE"
   - Click "Add to Browser" and confirm installation

## 🧪 Running the Tests

### Run All Tests
```bash
behave
```

### Run Specific Application Tests
```bash
# Run Jumia tests only
behave --tags=jumia

# Run GitHub tests only
behave --tags=github

# Run Refactory Academy tests only
behave --tags=refactory

# Run Shein tests only
behave --tags=shein

# Run SafeBoda tests only
behave --tags=safeboda

# Run YouTube Music tests only
behave --tags=youtube_music

# Run MovieBox tests only
behave --tags=moviebox
```

### Run Specific Feature Tags
```bash
# Run only search features
behave --tags=search

# Run only authentication features
behave --tags=authentication

# Run only payment features
behave --tags=payment
```

### Run with HTML Report
```bash
behave --format=html --outfile=test_report.html
```

### Run with Allure Report
```bash
behave --format=allure_behave.formatter:AllureFormatter --outfile=allure-results
allure serve allure-results
```

## 📝 Gherkin Keywords Used

### Given
- Used to set up the initial context and state
- Example: `Given User opens browser and navigates to Jumia website`

### When
- Used to describe actions that the user performs
- Example: `When User clicks on "Add to Cart" button`

### Then
- Used to describe expected outcomes and validations
- Example: `Then User should see "Item added to cart" confirmation message`

### And
- Used to add additional steps to Given, When, or Then
- Example: `And User should see product images and prices`

## 🏷️ Tagging System

The scenarios are organized using tags for easy filtering:

- **@search** - Search and browsing features
- **@authentication** - Login and registration features
- **@cart** - Shopping cart management
- **@checkout** - Payment and checkout processes
- **@account** - User account management
- **@reviews** - Rating and review features
- **@wishlist** - Wishlist management
- **@support** - Customer support features
- **@payment** - Payment processing
- **@tracking** - Order/ride tracking
- **@booking** - Booking and reservation features
- **@matching** - Driver/rider matching
- **@history** - Transaction history
- **@preferences** - User preferences
- **@cancellation** - Cancellation and refund features
- **@sharing** - Ride sharing features

## 🔧 Configuration

### Selenium IDE Configuration
The tests are designed to work with Selenium IDE browser extension:

1. Install Selenium IDE extension in your browser
2. Use the recording feature to capture test steps
3. Export tests as Python/Behave format
4. Replace placeholder steps in your feature files

### Recording Tests
1. Open Selenium IDE and start recording
2. Navigate to the website you want to test
3. Perform the actions described in the feature files
4. Stop recording and export as Python/Behave format
5. Replace the placeholder steps with actual recorded steps

### Test Data
- Test data is embedded in the scenarios
- Phone numbers, emails, and other data are examples
- Replace with actual test data for real applications

### Timeouts
- Default wait time: 10 seconds
- Can be modified in `WebDriverWait(driver, 10)`

## 📊 Test Coverage

### Feature Coverage Summary

| Application | Features | Scenarios | Coverage |
|-------------|----------|-----------|----------|
| Jumia | 8 | 20+ | E-commerce workflow |
| GitHub | 12 | 30+ | Development platform |
| Refactory Academy | 12 | 30+ | Educational learning platform |
| Shein | 12 | 30+ | Fashion e-commerce workflow |
| SafeBoda | 12 | 30+ | Ride-hailing and delivery |
| YouTube Music | 12 | 30+ | Music streaming platform |
| MovieBox | 12 | 30+ | Movie and TV streaming |

### Common Test Patterns

1. **User Registration Flow**
   - Account creation
   - Email/phone verification
   - Profile setup

2. **Authentication Flow**
   - Login with valid credentials
   - Login with invalid credentials
   - Password reset

3. **Search and Discovery**
   - Product/service search
   - Filtering and sorting
   - Category browsing

4. **Transaction Flow**
   - Add to cart/basket
   - Checkout process
   - Payment processing
   - Order confirmation

5. **User Management**
   - Profile updates
   - Settings management
   - History and receipts

## 🛠️ Customization

### Adding New Scenarios
1. Open the appropriate `.features` file
2. Add new scenario following Gherkin syntax
3. Implement corresponding step definitions in `comprehensive_steps.py`

### Adding New Applications
1. Create new `.features` file
2. Define scenarios using Gherkin syntax
3. Add step definitions to `comprehensive_steps.py`
4. Update the website navigation logic

### Modifying Existing Tests
1. Locate the scenario in the `.features` file
2. Modify the steps as needed
3. Update corresponding step definitions
4. Test the changes

## 📈 Best Practices

### Writing Good Scenarios
- Use clear, business-readable language
- Focus on behavior, not implementation
- Keep scenarios independent
- Use descriptive scenario names
- Include both positive and negative test cases

### Step Definitions
- Keep steps reusable
- Use parameterized steps where possible
- Handle exceptions gracefully
- Add appropriate waits and assertions

### Test Organization
- Group related scenarios with tags
- Use background steps for common setup
- Maintain consistent naming conventions
- Document complex scenarios

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver Issues**
   ```bash
   pip install --upgrade webdriver-manager
   ```

2. **Element Not Found**
   - Check if element selectors are correct
   - Verify page has loaded completely
   - Add appropriate waits

3. **Test Failures**
   - Check browser compatibility
   - Verify test data is valid
   - Review error messages in logs

### Debug Mode
Run tests with verbose output:
```bash
behave --verbose
```

## 📚 Additional Resources

- [Behave Documentation](https://behave.readthedocs.io/)
- [Selenium IDE Documentation](https://www.selenium.dev/selenium-ide/docs/en/introduction/getting-started)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)
- [BDD Best Practices](https://cucumber.io/docs/bdd/)
- [Selenium IDE Setup Guide](SELENIUM_IDE_SETUP.md)

## 🤝 Contributing

To contribute to this project:

1. Follow the existing code structure
2. Add appropriate tags to new scenarios
3. Update documentation
4. Test your changes thoroughly
5. Submit pull requests with clear descriptions

## 📄 License

This project is created for educational purposes as part of a classroom assignment.

---

**Note**: This project contains example scenarios and step definitions. For actual testing, replace example URLs and data with real application details. 
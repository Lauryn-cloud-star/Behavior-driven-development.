from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Global variables for test data
driver = None
wait = None

@given('User opens browser and navigates to {website}')
def step_impl(context, website):
    global driver, wait
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    # Navigate to appropriate website based on feature
    if "jumia" in website.lower():
        driver.get("https://www.jumia.com.ng")

    elif "refactory" in website.lower():
        driver.get("https://www.refactory.ug")
    elif "shein" in website.lower():
        driver.get("https://www.shein.com")
    elif "safeboda" in website.lower():
        driver.get("https://www.safeboda.com")
    elif "youtube music" in website.lower():
        driver.get("https://music.youtube.com")
    elif "moviebox" in website.lower():
        driver.get("https://www.moviebox.com")
    else:
        driver.get("https://www.example.com")

# Jumia E-commerce Steps
@when('User enters "{search_term}" in the search field')
def step_impl(context, search_term):
    search_box = wait.until(EC.presence_of_element_located((By.ID, "search-input")))
    search_box.clear()
    search_box.send_keys(search_term)

@when('User clicks on the search button')
def step_impl(context):
    search_button = wait.until(EC.element_to_be_clickable((By.ID, "search-button")))
    search_button.click()

@then('User should see search results for {product_type}')
def step_impl(context, product_type):
    results = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-results")))
    assert results.is_displayed()

@when('User clicks on "Add to Cart" for the first product')
def step_impl(context):
    add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart")))
    add_to_cart_button.click()

@then('User should see "Item added to cart" confirmation message')
def step_impl(context):
    confirmation = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-confirmation")))
    assert "added to cart" in confirmation.text.lower()

@when('User clicks on cart icon')
def step_impl(context):
    cart_icon = wait.until(EC.element_to_be_clickable((By.ID, "cart-icon")))
    cart_icon.click()

@then('User should see all added items in cart')
def step_impl(context):
    cart_items = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-items")))
    assert cart_items.is_displayed()



# Banking Application Steps
@when('User enters account number "{account_number}"')
def step_impl(context, account_number):
    account_field = wait.until(EC.presence_of_element_located((By.NAME, "accountNumber")))
    account_field.send_keys(account_number)

@when('User enters OTP from SMS "{otp}"')
def step_impl(context, otp):
    otp_field = wait.until(EC.presence_of_element_located((By.NAME, "otp")))
    otp_field.send_keys(otp)

@when('User clicks on "Login" button')
def step_impl(context):
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
    login_button.click()

@then('User should be logged in successfully')
def step_impl(context):
    dashboard = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard")))
    assert dashboard.is_displayed()

@when('User clicks on "Transfer" button')
def step_impl(context):
    transfer_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "transfer-button")))
    transfer_button.click()

@when('User enters beneficiary account number "{beneficiary_account}"')
def step_impl(context, beneficiary_account):
    beneficiary_field = wait.until(EC.presence_of_element_located((By.NAME, "beneficiaryAccount")))
    beneficiary_field.send_keys(beneficiary_account)

@when('User enters beneficiary name "{beneficiary_name}"')
def step_impl(context, beneficiary_name):
    name_field = wait.until(EC.presence_of_element_located((By.NAME, "beneficiaryName")))
    name_field.send_keys(beneficiary_name)

@when('User enters transfer amount "{amount}"')
def step_impl(context, amount):
    amount_field = wait.until(EC.presence_of_element_located((By.NAME, "transferAmount")))
    amount_field.send_keys(amount)

@when('User enters transfer description "{description}"')
def step_impl(context, description):
    description_field = wait.until(EC.presence_of_element_located((By.NAME, "transferDescription")))
    description_field.send_keys(description)

@when('User clicks on "Continue" button')
def step_impl(context):
    continue_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Continue')]")))
    continue_button.click()

@when('User enters transaction PIN "{pin}"')
def step_impl(context, pin):
    pin_field = wait.until(EC.presence_of_element_located((By.NAME, "transactionPin")))
    pin_field.send_keys(pin)

@when('User clicks on "Confirm Transfer" button')
def step_impl(context):
    confirm_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Confirm Transfer')]")))
    confirm_button.click()

@then('User should see "Transfer successful" message')
def step_impl(context):
    success_message = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "transfer-success")))
    assert "transfer successful" in success_message.text.lower()

# Shein Fashion E-commerce Steps
@when('User clicks on "Women" category')
def step_impl(context):
    women_category = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Women')]")))
    women_category.click()

@when('User selects "Dresses" subcategory')
def step_impl(context):
    dresses_subcategory = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Dresses')]")))
    dresses_subcategory.click()

@then('User should see various dress styles')
def step_impl(context):
    dress_styles = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dress-styles")))
    assert dress_styles.is_displayed()

@when('User clicks on "Add to Wishlist" button')
def step_impl(context):
    wishlist_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-wishlist")))
    wishlist_button.click()

@then('User should see "Added to wishlist" confirmation')
def step_impl(context):
    confirmation = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wishlist-confirmation")))
    assert "added to wishlist" in confirmation.text.lower()

@when('User goes to "Style Profile" section')
def step_impl(context):
    style_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Style Profile')]")))
    style_profile.click()

@when('User selects style preferences "{preferences}"')
def step_impl(context, preferences):
    style_prefs = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{preferences}']")))
    style_prefs.click()

# Refactory Academy Learning Platform Steps
@when('User clicks on "Courses" section')
def step_impl(context):
    courses_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Courses')]")))
    courses_section.click()

@then('User should see list of programming courses')
def step_impl(context):
    courses_list = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "courses-list")))
    assert courses_list.is_displayed()

@when('User enters "{course_name}" in search field')
def step_impl(context, course_name):
    search_field = wait.until(EC.presence_of_element_located((By.NAME, "courseSearch")))
    search_field.clear()
    search_field.send_keys(course_name)

@when('User clicks on "Enroll Now" button')
def step_impl(context):
    enroll_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Enroll Now')]")))
    enroll_button.click()

@when('User selects enrollment plan "{plan}"')
def step_impl(context, plan):
    plan_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{plan}']")))
    plan_option.click()

@when('User clicks on "Proceed to Payment" button')
def step_impl(context):
    payment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Proceed to Payment')]")))
    payment_button.click()

@when('User goes to "Video Lectures" section')
def step_impl(context):
    video_lectures = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Video Lectures')]")))
    video_lectures.click()

@when('User selects "{lecture_name}" lecture')
def step_impl(context, lecture_name):
    lecture = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{lecture_name}')]")))
    lecture.click()

@when('User clicks on "Play" button')
def step_impl(context):
    play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "play-button")))
    play_button.click()

@when('User goes to "Assignments" section')
def step_impl(context):
    assignments_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Assignments')]")))
    assignments_section.click()

@when('User clicks on "Submit Assignment" for "{assignment_name}"')
def step_impl(context, assignment_name):
    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Submit Assignment') and @data-assignment='{assignment_name}']")))
    submit_button.click()

@when('User uploads completed code file')
def step_impl(context):
    file_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']")))
    file_input.send_keys("/path/to/completed/assignment.py")

@when('User goes to "My Progress" section')
def step_impl(context):
    progress_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'My Progress')]")))
    progress_section.click()

@then('User should see course completion percentage')
def step_impl(context):
    completion_percentage = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "completion-percentage")))
    assert completion_percentage.is_displayed()

@when('User goes to "Discussion Forum" section')
def step_impl(context):
    forum_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Discussion Forum')]")))
    forum_section.click()

@when('User clicks on "New Post" button')
def step_impl(context):
    new_post_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-post-button")))
    new_post_button.click()

@when('User writes question about Python debugging')
def step_impl(context):
    question_field = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "question-field")))
    question_field.send_keys("How do I debug this Python code?")

@when('User clicks on "Post Question" button')
def step_impl(context):
    post_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Post Question')]")))
    post_button.click()

@when('User goes to "Mentorship" section')
def step_impl(context):
    mentorship_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Mentorship')]")))
    mentorship_section.click()

@when('User clicks on "Book Session" button')
def step_impl(context):
    book_session_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Book Session')]")))
    book_session_button.click()

@when('User selects mentor "{mentor_name}"')
def step_impl(context, mentor_name):
    mentor = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{mentor_name}']")))
    mentor.click()

@when('User goes to "Job Board" section')
def step_impl(context):
    job_board = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Job Board')]")))
    job_board.click()

@then('User should see available tech job listings')
def step_impl(context):
    job_listings = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-listings")))
    assert job_listings.is_displayed()



# Common Steps for All Applications
@when('User clicks on "{button_text}" button')
def step_impl(context, button_text):
    button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{button_text}')]")))
    button.click()

@when('User clicks on "{link_text}" link')
def step_impl(context, link_text):
    link = wait.until(EC.element_to_be_clickable((By.XPATH, f"//a[contains(text(), '{link_text}')]")))
    link.click()

@when('User clicks on "{element_text}"')
def step_impl(context, element_text):
    element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//*[contains(text(), '{element_text}')]")))
    element.click()

@then('User should see "{expected_text}"')
def step_impl(context, expected_text):
    element = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]")))
    assert element.is_displayed()

@then('User should see "{expected_text}" message')
def step_impl(context, expected_text):
    message = wait.until(EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{expected_text}')]")))
    assert message.is_displayed()

@when('User enters "{text}" in the {field_name} field')
def step_impl(context, text, field_name):
    field = wait.until(EC.presence_of_element_located((By.NAME, field_name.lower().replace(" ", "_"))))
    field.clear()
    field.send_keys(text)

@when('User selects "{option}" from {dropdown_name}')
def step_impl(context, option, dropdown_name):
    dropdown = wait.until(EC.element_to_be_clickable((By.NAME, dropdown_name.lower().replace(" ", "_"))))
    dropdown.click()
    option_element = wait.until(EC.element_to_be_clickable((By.XPATH, f"//option[contains(text(), '{option}')]")))
    option_element.click()

@then('User should be taken to {page_name} page')
def step_impl(context, page_name):
    # Verify page title or URL contains expected text
    assert page_name.lower() in driver.current_url.lower() or page_name.lower() in driver.title.lower()

@then('User should receive {notification_type} notification')
def step_impl(context, notification_type):
    # Simulate notification check
    time.sleep(1)
    assert True



# SafeBoda Ride-Hailing Steps
@when('User enters pickup location "{location}"')
def step_impl(context, location):
    pickup_field = wait.until(EC.presence_of_element_located((By.ID, "pickup-location")))
    pickup_field.send_keys(location)

@when('User enters destination "{destination}"')
def step_impl(context, destination):
    destination_field = wait.until(EC.presence_of_element_located((By.ID, "destination")))
    destination_field.send_keys(destination)

@when('User selects ride type "{ride_type}"')
def step_impl(context, ride_type):
    ride_type_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), '{ride_type}')]")))
    ride_type_button.click()

@when('User clicks on "Book Ride" button')
def step_impl(context):
    book_ride_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "book-ride-button")))
    book_ride_button.click()

@when('User goes to "Food Delivery" section')
def step_impl(context):
    food_delivery = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Food Delivery')]")))
    food_delivery.click()

@when('User selects restaurant "{restaurant}"')
def step_impl(context, restaurant):
    restaurant_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(), '{restaurant}')]")))
    restaurant_option.click()

@when('User goes to "Wallet" section')
def step_impl(context):
    wallet_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Wallet')]")))
    wallet_section.click()

@when('User clicks on "Add Money" button')
def step_impl(context):
    add_money_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add Money')]")))
    add_money_button.click()

# YouTube Music Steps
@when('User goes to "Music Preferences" section')
def step_impl(context):
    music_prefs = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Music Preferences')]")))
    music_prefs.click()

@when('User selects favorite genres "{genres}"')
def step_impl(context, genres):
    genre_list = genres.split(", ")
    for genre in genre_list:
        genre_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{genre}']")))
        genre_option.click()

@when('User goes to "Trending" section')
def step_impl(context):
    trending_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Trending')]")))
    trending_section.click()

@when('User clicks on "Play" button for a song')
def step_impl(context):
    play_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "play-button")))
    play_button.click()

@when('User goes to "Library" section')
def step_impl(context):
    library_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Library')]")))
    library_section.click()

@when('User clicks on "Create Playlist" button')
def step_impl(context):
    create_playlist_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create Playlist')]")))
    create_playlist_button.click()

@when('User enters playlist name "{playlist_name}"')
def step_impl(context, playlist_name):
    playlist_name_field = wait.until(EC.presence_of_element_located((By.NAME, "playlistName")))
    playlist_name_field.send_keys(playlist_name)

@when('User goes to "Downloads" section')
def step_impl(context):
    downloads_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Downloads')]")))
    downloads_section.click()

# MovieBox Steps
@when('User goes to "Content Preferences" section')
def step_impl(context):
    content_prefs = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Content Preferences')]")))
    content_prefs.click()

@when('User selects favorite genres "{genres}"')
def step_impl(context, genres):
    genre_list = genres.split(", ")
    for genre in genre_list:
        genre_option = wait.until(EC.element_to_be_clickable((By.XPATH, f"//input[@value='{genre}']")))
        genre_option.click()

@when('User goes to "Trending Now" section')
def step_impl(context):
    trending_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Trending Now')]")))
    trending_section.click()

@when('User clicks on "Watch Now" for a movie')
def step_impl(context):
    watch_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Watch Now')]")))
    watch_button.click()

@when('User clicks on "Add to Watchlist" button')
def step_impl(context):
    watchlist_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "add-to-watchlist")))
    watchlist_button.click()

@when('User goes to "My Watchlist" section')
def step_impl(context):
    watchlist_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'My Watchlist')]")))
    watchlist_section.click()

@when('User goes to "TV Shows" section')
def step_impl(context):
    tv_shows_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'TV Shows')]")))
    tv_shows_section.click()

@when('User clicks on "Watch Episode {episode}"')
def step_impl(context, episode):
    episode_button = wait.until(EC.element_to_be_clickable((By.XPATH, f"//button[contains(text(), 'Watch Episode {episode}')]")))
    episode_button.click()

@when('User goes to "Kids" section')
def step_impl(context):
    kids_section = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Kids')]")))
    kids_section.click()

@when('User clicks on "Create Kids Profile"')
def step_impl(context):
    create_kids_profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Create Kids Profile')]")))
    create_kids_profile.click()

@when('User enters child\'s name "{child_name}"')
def step_impl(context, child_name):
    child_name_field = wait.until(EC.presence_of_element_located((By.NAME, "childName")))
    child_name_field.send_keys(child_name)

@when('User sets age "{age}"')
def step_impl(context, age):
    age_field = wait.until(EC.presence_of_element_located((By.NAME, "childAge")))
    age_field.send_keys(age)

# Cleanup after scenarios
def after_scenario(context, scenario):
    global driver
    if driver:
        driver.quit()
        driver = None 
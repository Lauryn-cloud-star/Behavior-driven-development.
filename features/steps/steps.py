from behave import given, when, then

@given('User opens browser, enters URL and navigates to login page')
def step_impl(context):
    # Simulate opening browser and navigating to login page
    pass

@when('User enters data in Search field')
def step_impl(context):  # noqa: F811
    # Simulate entering data in search field
    pass

@when('User clicks on Search button')
def step_impl(context):  # noqa: F811
    # Simulate clicking search button
    pass

@when('User clicks on Add to cart for the first search result')
def step_impl(context):  # noqa: F811
    # Simulate adding first search result to cart
    pass

@when('User clicks on My Cart button')
def step_impl(context):  # noqa: F811
    # Simulate clicking on My Cart button
    pass

@then('User should get item added in Cart')
def step_impl(context):  # noqa: F811
    # Simulate checking item is in cart
    pass

@then('User should see price of item in front of item name')
def step_impl(context):  # noqa: F811
    # Simulate checking price is displayed
    pass

@when('User clicks on Purchase button')
def step_impl(context):  # noqa: F811
    # Simulate clicking purchase button
    pass

@when('User selects payment mode as Credit Card')
def step_impl(context):  # noqa: F811
    # Simulate selecting Credit Card as
    pass
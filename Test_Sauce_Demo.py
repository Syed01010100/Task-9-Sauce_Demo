from Sauce_Demo import SauceDemoAutomation
import pytest

@pytest.fixture
def setup_sauce_demo():
    demo = SauceDemoAutomation()
    demo.login()
    yield demo  # Pass the instance for testing



# Positive Test Case - Validate the URL
def test_positive_test_case_url(setup_sauce_demo):
    demo = setup_sauce_demo
    expected_url = "https://www.saucedemo.com/inventory.html"  # URL after logging in
    assert demo.fetch_url() == expected_url
    print(f"SUCCESS: Test URL {expected_url} passes the Positive Test Case")


# Positive Test Case - Validate the TITLE
def test_positive_test_case_title(setup_sauce_demo):
    demo = setup_sauce_demo
    expected_title = "Swag Labs"
    assert demo.fetch_title() == expected_title
    print(f"SUCCESS: Test Title '{expected_title}' passes the Positive Test Case")


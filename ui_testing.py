from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configure WebDriver to connect to Selenium Docker container
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run headlessly
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Connect to the Selenium container
driver = webdriver.Remote(
    command_executor="http://192.168.58.130:4444/wd/hub",  # Replace your-vagrant-ip with the IP of the VM
    options=chrome_options
)

try:
    # Navigate to your website hosted in staging/production
    driver.get("http://54.237.199.38:8083")  # Replace with the actual URL of your website

    # Check page title
    assert "Expected Title" in driver.title, f"Title mismatch: {driver.title}"

    # Validate header element
    header = driver.find_element(By.TAG_NAME, "h1")
    assert header.is_displayed(), "Header is not visible"
    print(f"Header Text: {header.text}")

    # Validate a button
    button = driver.find_element(By.ID, "submit")  # Replace 'submit' with actual button ID
    assert button.is_displayed() and button.is_enabled(), "Button is not functional"

    print("UI Tests Passed!")

except Exception as e:
    print(f"UI Test Failed: {e}")

finally:
    # Close the browser
    driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import chromedriver_autoinstaller

# Automatically install the correct version of ChromeDriver
chromedriver_autoinstaller.install()

# Set up the browser (Chrome in this case)
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run tests in headless mode
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Navigate to the website
    driver.get("http://192.168.58.130:8081")  # URL for development server
    time.sleep(2)  # Wait for page to load

    # Perform a UI check (example: verify the title)
    assert "Expected Title" in driver.title, "Title does not match!"

    # Check for a specific element (example: button)
    button = driver.find_element(By.ID, "submit-button")
    assert button.is_displayed(), "Submit button not found!"

    print("UI Tests Passed!")
except Exception as e:
    print(f"UI Test Failed: {str(e)}")
    exit(1)
finally:
    driver.quit()

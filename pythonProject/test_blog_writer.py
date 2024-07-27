from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver (assuming ChromeDriver is in your PATH)
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Set page load timeout
driver.set_page_load_timeout(60)

# Open the Blog Writer page
driver.get("jetbrains://pycharm/navigate/reference?project=pythonProject&path=index.html")  # Replace with the correct path to your HTML file


# Check authentication
def login():
    # This part depends on your authentication mechanism
    # Assuming a simple form submission for login
    if "login.html" in driver.current_url:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "loginButton")

        username_field.send_keys("your_username")
        password_field.send_keys("your_password")
        login_button.click()


# Call the login function
login()


# Add a new blog post
def add_blog_post(title, content):
    title_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "title"))
    )
    content_field = driver.find_element(By.ID, "content")
    publish_button = driver.find_element(By.CSS_SELECTOR, "#blogForm button[type='submit']")

    title_field.send_keys(title)
    content_field.send_keys(content)
    publish_button.click()


# Add a new comment to the latest blog post
def add_comment(comment):
    comment_form = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".comment-form"))
    )[-1]  # Select the last comment form
    comment_textarea = comment_form.find_element(By.TAG_NAME, "textarea")
    submit_button = comment_form.find_element(By.TAG_NAME, "button")

    comment_textarea.send_keys(comment)
    submit_button.click()


# Rate the latest blog post with 5 stars
def rate_post():
    rating_stars = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".rating"))
    )[-1].find_elements(By.TAG_NAME, "span")
    for star in rating_stars:
        ActionChains(driver).move_to_element(star).click().perform()
        time.sleep(0.5)  # Wait a bit to see the rating effect


# Example usage
add_blog_post("Test Title", "This is a test blog post content.")
time.sleep(2)  # Wait for the post to be added
add_comment("This is a test comment.")
time.sleep(2)  # Wait for the comment to be added
rate_post()
time.sleep(2)  # Wait for the rating to be applied

# Close the WebDriver
driver.quit()

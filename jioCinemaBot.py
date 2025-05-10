# jioCinemaBot.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

def test_case(description, func):
    try:
        func()
        print(f"Test '{description}' passed")
    except Exception as e:
        print(f"Test '{description}' failed: {e}")

# Opening of the JioCinema website
url = "https://www.jiocinema.com/"
driver.get(url)
time.sleep(5)  # Giving some time to load the page

# Test Case 1: Verify if the JioCinema logo is present on the homepage
def verify_logo_presence():
    logo = driver.find_element(By.XPATH, "//img[@alt='JioCinema']")
    assert logo.is_displayed()

test_case("Verify JioCinema logo presence", verify_logo_presence)

# Test Case 2: Entering an invalid movie name in the search box
def invalid_search():
    search_input_box = driver.find_element(By.XPATH, "//input[@id='searchInputBox']")
    search_input_box.clear()
    search_input_box.send_keys("invalidmoviename")
    search_input_box.send_keys(Keys.RETURN)
    time.sleep(5)
    # Check if no search results message is displayed
    no_results_message = driver.find_element(By.XPATH, "//div[contains(text(), 'No results found')]")
    assert no_results_message.is_displayed()
#test_case("Invalid Search",invalid_search)

# Test Case 3: Entering the movie name "english vinglish" in the search box
def search_movie():
    search_input_box = driver.find_element(By.XPATH, "//input[@id='searchInputBox']")
    search_input_box.send_keys("english vinglish")
    search_input_box.send_keys(Keys.RETURN)
    time.sleep(5)

test_case("Search for the movie 'English Vinglish'", search_movie)

# Test Case 4: Opening the page for "english vinglish"
def open_movie_page():
    movie_link = driver.find_element(By.XPATH, "//a[@aria-label='English Vinglish (2012) Hindi Movie: Watch Full HD Movie Online On JioCinema']//div[@class='mui-style-1v5keco-gradient']")
    movie_link.click()
    time.sleep(10)

test_case("Open the 'English Vinglish' movie page", open_movie_page)

# Test Case 5: Starting the movie "english vinglish"
def start_movie():
    play_button = driver.find_element(By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1Bold mui-style-6z4y8n']")  # Adjust the class name as necessary
    play_button.click()
    time.sleep(60) 

test_case("Start the movie 'English Vinglish'", start_movie)

# Close the WebDriver
driver.quit()

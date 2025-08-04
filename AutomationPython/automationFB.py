import time
import pickle
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

COOKIES_FILE = "facebook_cookies_firefox.pkl"
FACEBOOK_URL = "https://www.facebook.com/"
FB_BUSINESS_PLANNER_URL = "https://business.facebook.com/latest/planner"

def save_cookies(driver, path):
    with open(path, "wb") as file:
        pickle.dump(driver.get_cookies(), file)
    print("✅ Cookies saved.")

def load_cookies(driver, path):
    with open(path, "rb") as file:
        cookies = pickle.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    print("✅ Cookies loaded.")

def manual_login(driver):
    driver.get(FACEBOOK_URL)
    input("🔐 Please log in manually and press Enter here...")
    save_cookies(driver, COOKIES_FILE)

def schedule_post(driver, wait, content, date_str, time_str):
    driver.get(FB_BUSINESS_PLANNER_URL)

    # Wait until the Create Post button is clickable and click it
    create_post_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Create post']")))
    create_post_btn.click()

    # Wait for post input box
    textbox = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']")))
    textbox.clear()
    textbox.send_keys(content)

    # Click Schedule option
    schedule_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Schedule')]")))
    schedule_option.click()

    # Fill date and time (you may need to adjust these selectors for Facebook's UI)
    date_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Date']")))
    time_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Time']")))

    date_input.clear()
    date_input.send_keys(date_str)

    time_input.clear()
    time_input.send_keys(time_str)

    # Click the Schedule button
    schedule_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Schedule post')]")))
    schedule_btn.click()

    print(f"✅ Scheduled post: '{content[:20]}...' at {date_str} {time_str}")

    time.sleep(5)  # Wait a bit before next iteration to ensure scheduling finishes

def main():
    driver = webdriver.Firefox()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)  # <-- Create wait here, using this driver

    if os.path.exists(COOKIES_FILE):
        driver.get(FACEBOOK_URL)
        time.sleep(3)
        load_cookies(driver, COOKIES_FILE)
        driver.get(FB_BUSINESS_PLANNER_URL)
        time.sleep(5)
    else:
        manual_login(driver)

    df = pd.read_excel("post.xlsx")  # Your Excel with columns like 'content', 'date', 'time'

    for _, row in df.iterrows():
        try:
            schedule_post(driver, wait, row['Content'], row['Date'], row['Time'])
        except TimeoutException:
            print("❌ Some element was not found or clickable. Stopping automation.")
            break

    driver.quit()

if __name__ == "__main__":
    main()

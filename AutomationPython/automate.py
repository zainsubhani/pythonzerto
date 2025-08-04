from selenium.webdriver.chrome.options import Options as FirefoxOptions
from selenium import webdriver

chromBrowser = webdriver.Firefox()
# /user/local/bin

chromBrowser.get('https://www.facebook.com/')
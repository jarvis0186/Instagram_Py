from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class setup_driver:

    def setup_driver(self, config):
            driver = webdriver.Chrome(config["driver_path"])
            driver.get(config["url"])
            return driver
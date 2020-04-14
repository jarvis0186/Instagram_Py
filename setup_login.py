import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class login:

    def setup_driver(self, config):
        driver = webdriver.Chrome(config["driver_path"])
        driver.get(config["url"])
        return driver

    def login_profile(self, config):
        driver = self.setup_driver(config)
        
        try:
            element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input" )) 
        )
        except:
            print("WebDriverWait timed out: couldn't find search bar" )

        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(config["username"]) #types user name

        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(config["password"]) #types password

        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/article/div[2]/div[1]/div/form/div[4]/button").click() #Clicks the login button

        return driver
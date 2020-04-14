import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_config import *
from setup_login import *

def addFollowers(config):

    login_prof = login()
    driver = login_prof.login_profile(config)

    time.sleep(1)

    try:
        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[3]/button[2]" )) 
    )
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
    except: 
        print("No notification pop up! " )

    driver.get(config["explore_url"])

    time.sleep(1)

    count = temp = 0
    while(count!=10):
        try:
            element = WebDriverWait(driver, 4).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div["+str(count+1)+"]/div[3]/button" )) 
             )
            if(temp == 10):
                time.sleep(300)
                temp=0
            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div["+str(count+1)+"]/div[3]/button").click() #Click follow
            
            time.sleep(2)
            if(str(driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div["+str(count+1)+"]/div[3]/button").text) == "Following"):
                prof_id = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div["+str(count+1)+"]/div[2]/div[1]").get_attribute("id")
                print(prof_id)
                driver.find_element_by_xpath("//*[@id=\""+str(prof_id).strip()+"\"]/div/a").click()
                time.sleep(2)
                try:
                    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/article/div/div/div/div[1]/a/div[1]/div[2]").click() #Clicks on the first pic
                    time.sleep(1)
                    try:
                        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button").click() #Likes one of their pics
                        time.sleep(1)
                        driver.back()
                        driver.back()
                    except:
                        driver.back()
                        driver.back()
                except:
                    driver.back()
            else:
                continue
            count+=1
            temp+=1
        except: 
            print("There was an error following new people.!" )


def main():

    con = config_ini()
    config = con.read_config()

    addFollowers(config)

if __name__ == "__main__":
    main()

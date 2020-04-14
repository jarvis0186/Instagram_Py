import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class unfollow:

#---------------------------------------------------------Unfollows profiles that we are following!---------------------------------------------------------------------------------------------------------------------
    
    def unfollow_profiles(self,profile_name, config, driver):

        #--------------------------------------------------------------------------- Waits to find the search bar and types Profile name ---------------------------------------------------------------------------------------------------
        time.sleep(2)

        try:
            element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[3]/button[2]" )) 
        )
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()
        except: 
            print("No notification pop up! " )

        try:
            element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div" )) 
        )
        except:
            print("WebDriverWait timed out: couldn't find search bar" )

        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div").click()

        search_bar = driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/input")

        search_bar.clear()
        search_bar.send_keys(profile_name) #types in the user name
        # ---------------------------------------------------------------------------- Checks if that user profile is present! ----------------------------------------------------------------------------------------
        try:
            element = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div"))
        )
        except:
            print("WebDriverWait timed out: couldn't find user profile" )

        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click() #Clicks the particular user profile.

        #----------------------------------------------------------------------------- Checks if we are following that user profiles -----------------------------------------------------------------------------------
        try:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button/div/span"))
        )
            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/div[1]/div[2]/span/span[1]/button").click() #clicks to find the unfollow button
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[1]").click() #Clicks on unfollow

        except:
            print("We do not follow : " + profile_name)
            
        #-------------------------------------------------------------------------------- Goes to the home page to get one with the next user! ----------------------------------------------------------------------
        try:
            element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a"))
        )
        except:
            print("WebDriverWait timed out: couldn't find home button" )


        driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[3]/div/div[1]/div/a").click()
        

        
            

        

        

            



        

    


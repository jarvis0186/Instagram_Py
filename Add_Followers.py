import requests
import time
import sys
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from read_config import *
from setup_login import *
from setup_driver import *


def addFollowers(config):

    setupDriver = setup_driver() #Creating instances
    login_prof = login()
    driver = setupDriver.setup_driver(config) #Initializes driver.

    driver = login_prof.login_profile(config, driver) #Logs into profile

    time.sleep(2)

    try:
        element = WebDriverWait(driver, 2).until(
        EC.presence_of_element_located((By.XPATH,"/html/body/div[4]/div/div/div[3]/button[2]" )) 
    )
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click() 
    except: 
        print("No notification pop up! " )

    max_count = 3

    while(max_count>0):
        choice_input = int(input("Choose an option from below:\n1.To follow people from likes of a well known page.\n2.To follow people according to hashtags.\n3.To follow people from insta suggestions.\nPlease type your reply as 1 or 2 or 3:\t"))
        max_count-=1
        #-------------------------------------------------------------------------------------------------CHECKS FOR POP UP NOTIFICATION--------------------------------------------------------------------------------
        

        if(choice_input == 1):
            print("\nThis method is still a lil glitchy but works good enough to fool insta!!! :P\n")
            max_count=0

            profile_name = str(input("\nEnter the username of the page: "))
            total_no_of_followers = int(input("Enter the number of followers you wish to follow: "))

            count=real_count=total_tries = 1

            print("Profile name enterd: " + profile_name)

            time.sleep(1)

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
            time.sleep(2)

            try:
                element = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div"))
            )
            except:
                print("WebDriverWait timed out: couldn't find user profile" )

            driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div").click() #Clicks the particular user profile.
            time.sleep(2)

            pic_to_click = 1 #random.randrange(1,3,1)

            print("Following people from picture number : " + str(pic_to_click)) 
            try:
                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-root\"]/section/main/div/div[3]/article/div[1]/div/div[1]/div["+str(pic_to_click)+"]/a/div/div[2]"))
                )
                driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[3]/article/div[1]/div/div[1]/div["+str(pic_to_click)+"]/a/div/div[2]").click()
                
            except:
                try:
                    element = WebDriverWait(driver, 3).until(
                        EC.presence_of_element_located((By.XPATH, "//*[@id=\"react-root\"]/section/main/div/div[2]/article/div[1]/div/div[1]/div["+str(pic_to_click)+"]/a/div/div[2]"))
                    )
                    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/article/div[1]/div/div[1]/div["+str(pic_to_click)+"]/a/div/div[2]").click()
                except:
                    print("Cannot click photo number : " + str(pic_to_click) + " of profile: "+ profile_name)

            time.sleep(2)
            #---------------------------------------------------------The pic might either have common likes or might be a brand new profile. so the position of the like button matters-------------------------------
            try:
                element = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button"))
                )
                driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div[2]/button").click()
                                            
            except:
                try:
                    element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button"))
                    )
                    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[2]/div/div/button").click()
                except:
                    print("Cannot open the likes of this picture")
            while(total_tries<=total_no_of_followers):
                if(total_tries%10 == 0):
                    print("Followed upto 10 profiles so taking a nap for 5 minutes...")
                    t=300
                    while t:
                        mins, secs = divmod(t, 60)
                        timeformat = '{:02d}:{:02d}'.format(mins, secs)
                        print(timeformat, end='\r')
                        time.sleep(1)
                        t -= 1
                if(count == 10):
                    count = 7
                    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div["+str(count)+"]/div[3]/button").send_keys(Keys.PAGE_DOWN)
                    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div["+str(count)+"]/div[3]/button").send_keys(Keys.PAGE_DOWN)
                try:  
                    element = WebDriverWait(driver, 25).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div["+str(count)+"]/div[3]/button"))
                    )
                    driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div/div["+str(count)+"]/div[3]/button").click() #Follows number of people specified
                    count+=1
                    real_count+=1
                    try:
                        element = WebDriverWait(driver, 1).until(
                        EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div/div/div[3]/button[2]"))
                        )
                        driver.find_element_by_xpath("/html/body/div[6]/div/div/div[3]/button[2]").click() #Click on cancel if already following
                        real_count-=1
                    except:
                        pass
                    time.sleep(2)
                except Exception as e:
                    print("There was an error in following people, The error is --> " + str(e))
                total_tries+=1

            print("Total number of people followed: " + str(real_count-1))
                
            

        elif(choice_input == 2):

            hashtag_list = list(map(str, input("\nEnter upto 4 hashtags separated by space:\n").split()))
            print(hashtag_list)
            max_count=0

        #---------------------------------------------------------------------------------------------FOLLOWS INSTA SUGGESTED PEOPLE--------------------------------------------------------------------------------------
        elif(choice_input == 3):
            
            time.sleep(1)

            max_count = 0

            total_no_of_followers = int(input("Enter the number of followers you wish to follow: "))

            driver.get(config["explore_url"]) #Redirects to suggestions page

            time.sleep(1)

            count = 1
            
            while(count<=total_no_of_followers):
                try:
                    element = WebDriverWait(driver, 4).until(
                        EC.presence_of_element_located((By.XPATH,"//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div["+str(count)+"]/div[3]/button" )) #Checks if a new person is there to follow
                    )
                    if(count%10 == 0):
                        print("Followed upto 10 profiles so taking a nap for 5 minutes...")
                        t=300
                        while t:
                            mins, secs = divmod(t, 60)
                            timeformat = '{:02d}:{:02d}'.format(mins, secs)
                            print(timeformat, end='\r')
                            time.sleep(1)
                            t -= 1

                    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div["+str(count)+"]/div[3]/button").click() #Click follow
                    
                    time.sleep(2)
                    if(str(driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div["+str(count)+"]/div[3]/button").text) == "Following"): #Checks if its an open account
                        prof_id = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[2]/div/div/div["+str(count)+"]/div[2]/div[1]").get_attribute("id") #Gets the ID of the person
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
                    count+=1
                except: 
                    print("There was an error following new people.!" )

            print("Total number of people followed : " + str(count))

            
        else:
            if(max_count>=2):
                print("\nPlease recheck your input...\nYou will be prompted again in 5 seconds , make sure to mention either 1 or 2 or 3 only as your input\n")
                time.sleep(5)
            elif(max_count >=1):
                print("\nLast try please enter the correct format of input...\nYou might have to re run the code if there is an error.\n")
                time.sleep(5)
            else:
                print("\nPlease re-run the code....")
def main():

    con = config_ini()
    config = con.read_config()

    addFollowers(config)

if __name__ == "__main__":
    main()

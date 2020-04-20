import instaloader
import configparser
import time
from Unfollow_Profiles import *
from setup_login import *
from read_config import *
from setup_driver import *

def main():
    followers_list = []
    following_list = []
    not_followers_list = []
    con = config_ini()

    config= con.read_config()

    exception_list = open("Exceptions_list.txt", "r").read().split("\n")

    insta_obj = instaloader.Instaloader()

    insta_obj.login(config["username"], config["password"])
    print("Yay login success")
    profile = instaloader.Profile.from_username(insta_obj.context, config["username"])

   
    followers = profile.get_followers()
    print("Reading followers successful")
    followees = profile.get_followees()
    print("Reading followees successful")

    print("Evaluating the total number count...")
#--------------------------------------------------------------------- GET FOLLOWERS LIST -----------------------------------------------------------------------------------------------------------------------------------------
    for i in followers:
        followers_list.append(i)

#--------------------------------------------------------------------- GET FOLLOWING LIST -----------------------------------------------------------------------------------------------------------------------------------------
    for i in followees:
        following_list.append(i)

#--------------------------------------------------------------------- GET UNWANTED FOLLOWING LIST -----------------------------------------------------------------------------------------------------------------------------------------
    for i in following_list:
        profile_username = str(i).split("Profile")[1].split("(")[0].strip()
        if(i in followers_list or profile_username in exception_list):
            continue
        else:
            not_followers_list.append(profile_username)

    print("Number of followers --> " + str(len(followers_list)))
    print("Number of followees --> " + str(len(following_list)))
    print("Number of people who we follow but they don't --> " + str(len(not_followers_list)))

    # f = open("not_follwers_list.txt", "r")
    # string_useless = f.read()
    # not_followers_list = string_useless.split("\n")
    
    setupDriver = setup_driver() #Creating instances
    login_prof = login()
    driver = setupDriver.setup_driver(config) #Initializes driver.

    driver = login_prof.login_profile(config, driver) #Logs into profile
    unfollow_profile = unfollow()

    unfollow_count = temp = 0
    total_unfollow_count = 120
    if(len(not_followers_list)< total_unfollow_count):
        total_unfollow_count = len(not_followers_list)
    Notification_Flag=False #Checks for the notification pop up
    for i in not_followers_list[::-1]:
        if i in exception_list:
            pass
        elif(unfollow_count == total_unfollow_count):
            break
        else:
            unfollow_profile.unfollow_profiles(i, config, driver, Notification_Flag)
            unfollow_count+=1
            temp+=1
            if(temp == total_unfollow_count//3):
                print("Deleting cookies...")
                driver.delete_all_cookies()
                print("Cookies Deleted...\nRe-Login... Beta mode, this may not work!!")
                driver.get(config["url"])
                driver = login_prof.login_profile(config, driver)
                temp=0
                
            if(unfollow_count % 8 == 0):
                t = 600
                print("Unfollowed about 8 people...Sleeping for "+ str(t) + " seconds")
                while t:
                    mins, secs = divmod(t, 60)
                    timeformat = '{:02d}:{:02d}'.format(mins, secs)
                    print(timeformat, end='\r')
                    time.sleep(1)
                    t -= 1 #Sleep for 5 minutes if you have unfollowed 10 people
        Notification_Flag=True

    print("Total number of people unfollowed --> " + str(unfollow_count))

    driver.close()
if __name__ == "__main__":
    main()

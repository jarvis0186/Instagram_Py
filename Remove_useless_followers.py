import instaloader
import configparser
import time
from Unfollow_Profiles import *
from setup_login import *
from read_config import *

def main():
    followers_list = []
    following_list = []
    not_followers_list = []
    con = config_ini()

    config= con.read_config()

    exception_list = open("Exceptions_list.txt", "r").read().split("\n")

    insta_obj = instaloader.Instaloader()

    insta_obj.login(config["username"], config["password"])

    profile = instaloader.Profile.from_username(insta_obj.context, "bikers_and_trippers")

    followers = profile.get_followers()
    followees = profile.get_followees()

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

    # f = open("not_follwers_list.txt", "r")
    # string_useless = f.read()
    # not_followers_list = string_useless.split("\n")
    
    login_prof = login()
    unfollow_profile = unfollow()

    driver = login_prof.login_profile(config)

    unfollow_count = 0
    for i in not_followers_list:
        if i in exception_list:
            pass
        else:
            unfollow_profile.unfollow_profiles(i, config, driver)
            unfollow_count+=1
            if(unfollow_count == 10):
                time.sleep(600) #Sleep for 10 minutes if you have unfollowed 10 people


if __name__ == "__main__":
    main()

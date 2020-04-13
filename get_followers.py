import instaloader

insta_obj = instaloader.Instaloader()

insta_obj.login("bikers_and_trippers", "DominateToFlyBy")

profile = instaloader.Profile.from_username(insta_obj.context, "bikers_and_trippers")

followers = profile.get_followers()
followees = profile.get_followees()

followers_list = []
following_list = []

not_followers_list = []

for i in followers:
    followers_list.append(i)

for i in followees:
    following_list.append(i)


for i in following_list:
    if(i in followers_list):
        continue
    else:
        not_followers_list.append(i)


for i in not_followers_list:
    print(str(i).split("Profile")[1].split("(")[0].strip())
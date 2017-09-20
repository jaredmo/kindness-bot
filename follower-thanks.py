# Import modules and Twitter credentials
import os
import tweepy
from credentials import *


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Create text file for followers if it doesn't exist
if not os.path.exists("follower_ids.txt"):
    f = open("follower_ids.txt", '+w')
    f.close()


#Read existing id's into a list
f = open("follower_ids.txt", "r")
user_list = f.readlines()
f.close()


#Strip out \n from user_list
user_list = list(map(lambda x:x.strip(),user_list))


#Send new followers a reply and add id to follower_ids.txt
print("Sending new followers a reply. Writing id to file...")
for follower in tweepy.Cursor(api.followers).items():
    if follower.id_str not in user_list:
        print(follower.id, follower.name)
        sn = follower.screen_name
        m = "@%s Thanks for the follow. Remember to always be nice online!" % (sn)
        api.update_status(m)
        f = open("follower_ids.txt", "a")
        f.write(follower.id_str + '\n')
        f.close()

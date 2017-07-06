# Import modules and Twitter credentials
import tweepy
from time import sleep
from credentials import *


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Open text file and import each line
f = open('kind-tweets.txt', 'r')
file_lines = f.readlines()
f.close()


# Tweet a line every 30 minutes
def tweet():
    for line in file_lines:
        try:
             print(line)
             if line != '\n':
                 api.update_status(line)
                 sleep(900)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

tweet()
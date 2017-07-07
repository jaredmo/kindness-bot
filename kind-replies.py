# Import modules and Twitter credentials
import tweepy
import os
from credentials import *
from time import sleep
import datetime
from datetime import timedelta
from dateutil.parser import parser


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Write the current datetime to text file for reference
f = open("last-run.txt", '+w')
f.write(str(datetime.datetime.now()))
f.close()


# Create the file that will house last tweet ID searched
if not os.path.exists("last-tweet.txt"):
    f = open("last-tweet.txt", '+w')
    f.write(str(0))
    f.close()


# Read in last tweet ID
f = open("last-tweet.txt", 'r')
maxtweet = int(f.readline())
f.close()
print("Let's begin searching for meanie pants at tweet ID:", maxtweet)


# Create search criteria
txt = "'you are' pathetic OR dumb"
gc = '36.1613195,-86.7811641,200km'
print("Searching on", txt)


# It's kindness time, Nashville...
for tweet in tweepy.Cursor(api.search,
                     q=txt,
                     since_id=maxtweet,
                     geocode=gc).items(50):
    if tweet.text[:2] != "RT":
        print("Sending kindness reminder to", tweet.user.screen_name, "@ tweet ID:", tweet.id)
        sn = tweet.user.screen_name
        m = "@%s Friendly reminder to always be nice online!" % (sn)
        api.update_status(m, tweet.id)
        print("Napping for 2 minutes so Twitter doesn't get ANGRY. Zzzzzz...")
        if tweet.id > maxtweet:
            maxtweet = tweet.id
        sleep(120)

#Write out the last tweet ID for next run
print("Last tweet searched is", maxtweet, "...Writing to file...")
f = open("last-tweet.txt", '+w')
f.write(str(maxtweet))
f.close()


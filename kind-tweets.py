# Import modules and Twitter credentials
import tweepy
from time import sleep
from credentials import *
from shutil import copyfile
import os
import datetime


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


# Open text file and import each line
f = open(path + "\kind-tweets.txt", "r")
file_lines = f.readlines()
f.close()


# Tweet a line every 15 minutes
def tweet():
    for line in file_lines:
        print("Sending this kind tweet:", line)
        if line != '\n':
            api.update_status(line)
            print("Napping for 15 minutes. Zzzzzz...")
            sleep(900)
        else:
            pass
tweet()

# Create text file for tweet archive if it doesn't exist
if not os.path.exists("kind-tweets-archive.txt"):
    f = open("kind-tweets-archive.txt", '+w')
    f.close()

# Archive tweets and clear file
f = open(path + "\kind-tweets.txt", "r")
archive = f.readlines()
f.close()
if archive:
    f = open("kind-tweets-archive.txt", "a")
    f.write(str(datetime.datetime.now()) + "\n")
    f.writelines(archive)
    f.write("\n")
    f.close()
    os.remove(path + "\kind-tweets.txt")
    open(path + "\kind-tweets.txt", '+w')

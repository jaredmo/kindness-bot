# Import modules and Twitter credentials
import tweepy
from credentials import *


# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


#Monitor rate limits
data = api.rate_limit_status()
print(data['resources']['search']['/search/tweets'])
print(data['resources']['users']['/users/lookup'])
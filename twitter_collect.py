import tweepy
import configparser

# Read config file
config = configparser.ConfigParser()
config.read('config.ini')

# Authentication Details
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) # We use this to get access to our twitter account

public_tweets = api.home_timeline() # This will get the last 20 tweets from our timeline
for tweet in public_tweets:
    print(tweet.text)

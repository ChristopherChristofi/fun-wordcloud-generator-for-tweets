# Twitter API authentication

from dotenv import load_dotenv
import os
import tweepy

load_dotenv()

consumer_key = os.getenv('API_KEY')
consumer_secret_key = os.getenv('API_SECRET_KEY')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# authorize the API key
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret_key)

# authorization to user's access token and access token secret
authentication.set_access_token(access_token, access_token_secret)

# call the api
api = tweepy.API(authentication)
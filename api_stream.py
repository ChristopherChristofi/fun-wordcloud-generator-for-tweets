import tweepy
import time
from api_auth import api
from api_utilities import parse_hashtags
from database_queries import insertCommand
from database_config import build

class FootballStream(tweepy.StreamListener):
    '''Stream class'''

    def __init__(self, time_limit=120):
        self.start_time = time.time()
        self.limit = time_limit
        super(FootballStream, self).__init__()

    def on_connect(self):
        print("Successfully connected to Twitter API.")

    def on_status(self, status):

        # Tweet ID
        tweet_id = status.id
        # User ID
        user_id = status.user.id
        # Username
        username = status.user.name

        # Qualify tweet character length
        if status.truncated == True:
            tweet = status.extended_tweet['full_text']
            hashtags = status.extended_tweet['entities']['hashtags']
        else:
            tweet = status.text
            hashtags = status.entities['hashtags']

        # Parse incoming entity variables
        hashtags = parse_hashtags(hashtags)

        # Select retweet counts
        retweet_count = status.retweet_count
        # Select language
        lang = status.lang

        # Qualify tweet is in English and not a retweet
        if not hasattr(status, "retweeted_status") and lang=="en":
            # Call sql command
            insertCommand(user_id, username, tweet_id, tweet, retweet_count, hashtags)

        # Validate timelimit for streaming processes
        if (time.time() - self.start_time) > self.limit:
            # On completion of timelimit
            print(time.time(), self.start_time, self.limit)
            return False

    # Handle too many request error status
    def on_error(self, status_code):
        if status_code == 420:
            # Returning False in on_data disconnects the stream
            return False

def run():

    build()

    '''Function to initiate stream'''
    FootballStreamListener = FootballStream()
    set_stream = tweepy.Stream(auth=api.auth, listener=FootballStreamListener, tweet_mode="extended")
    set_stream.filter(track=['FFC','FulhamFootballClub','FulhamFC'])

run()
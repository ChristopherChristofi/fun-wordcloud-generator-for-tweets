import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
port = os.getenv('PORT')
database = os.getenv('DB')
user = os.getenv('USER')
passw = os.getenv('PASS')

def insertCommand(user_id, user_name, tweet_id, tweet, retweet_count, hashtags):

    db = psycopg2.connect(host=host,database=database,port=port,user=user,password=passw)

    command_handler = db.cursor()

    # create sql instruction for user information insert
    sql = '''INSERT INTO twitter_users (user_id, user_name) VALUES (%s,%s) ON CONFLICT
                 (user_id) DO NOTHING;'''
    command_handler.execute(sql,(user_id,user_name))

    # create sql instruction for tweet information insert
    sql = '''INSERT INTO user_tweets (tweet_id, user_id, tweet, retweet_count) VALUES (%s,%s,%s,%s);'''
    command_handler.execute(sql,(tweet_id, user_id, tweet, retweet_count))

    # create sql instruction for entity information insert
    for i in range(len(hashtags)):
        hashtag = hashtags[i]
        sql = '''INSERT INTO tweet_entities (tweet_id, hashtag) VALUES (%s,%s);'''
        command_handler.execute(sql,(tweet_id, hashtag))

    db.commit()
    command_handler.close()
    db.close()

def queryCommand(query):

    db = psycopg2.connect(host=host,database=database,port=port,user=user,password=passw)

    command_handler = db.cursor()

    command_handler.execute(query)

    rows = command_handler.fetchall()

    return rows
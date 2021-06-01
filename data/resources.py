import os
from dotenv import load_dotenv

load_dotenv()

raw_searched_data = os.getenv("RAW_JSON") or "./data/raw_data/raw_tweets.jsonl"
raw_processed_data = "./data/raw_data/raw_processed_tweets.jsonl"
raw_csv_data = "./data/raw_data/raw_processed_tweets.csv"
# raw_database_path AND raw_database_path_config MUST match
raw_database_path_config = "database/raw/raw_extraction.db"
raw_database_path = "./database/raw/raw_extraction.db"
raw_datatable_headers = ['user_id', 'tweet_id', 'tweet_date', 'tweet_text', 'tweet_lang']
raw_tablename = "rawtwittertweet"

stage_db_user=os.getenv("STAGE_USER") or "CHANGEME"
stage_db_pass=os.getenv("STAGE_PASS") or "CHANGEME"
stage_db_host=os.getenv("STAGE_HOST") or "CHANGME"
stage_db_port=os.getenv("STAGE_PORT") or "CHANGME"
stage_db_name = "stage_database"
stage_user_table = "twitteruser"
stage_tweet_table = "twittertweet"
stage_date_table = "tweetdate"
stage_tweet_csv = "./data/stage_data/stage_tweets.csv"
stage_date_csv = "./data/stage_data/stage_dates.csv"
stage_user_csv = "./data/stage_data/stage_users.csv"
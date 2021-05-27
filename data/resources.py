import os
from dotenv import load_dotenv

load_dotenv()

raw_searched_data = os.getenv("RAW_JSON") or "./data/raw_data/raw_tweets.jsonl"
raw_processed_data = "./data/raw_data/raw_processed_tweets.jsonl"
raw_csv_data = "./data/raw_data/raw_processed_tweets.csv"
# raw_database_path AND raw_database_path_config MUST match
raw_database_path_config = "data/database/raw/raw_extraction.db"
raw_database_path = "./data/database/raw/raw_extraction.db"
raw_datatable_headers = ['user_id', 'tweet_id', 'tweet_date', 'tweet_text', 'tweet_lang']

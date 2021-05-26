import os
from dotenv import load_dotenv

load_dotenv()

topic = os.getenv("TAG") or "Football"

raw_search_msg = "Will takes some time. Searching for tweets with tag topic: {topic}".format(topic=topic)
raw_retweet_process_msg = "Raw data process initiated. Retweets to be removed."
raw_csv_conversion_msg = "Converting processed raw data, no retweets, into csv."
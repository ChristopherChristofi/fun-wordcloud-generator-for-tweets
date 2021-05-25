import os
from dotenv import load_dotenv
from raw_processing.raw_utilities import raw_search_twitter, raw_remove_retweets, raw_csv_conversion

load_dotenv()

topic = os.getenv("TAG") or "Football"
raw_search_msg = "Will takes some time. Searching for tweets with tag topic: {topic}".format(topic=topic)
raw_retweet_process_msg = "Raw data process initiated. Retweets to be removed."
raw_csv_conversion_msg = "Converting processed raw data, no retweets, into csv."

print('')
print('[1] Search twitter API for football topic')
print('[2] Remove retweets from existing raw JSON data')
print('[3] Convert processed raw data to CSV file')
print('[0] To exit program')
print('')

start = 1
while start == True:
    input_option = int(input('Which option>'))
    if input_option == 1:
        print(raw_search_msg)
        raw_search_twitter()
    if input_option == 2:
        print(raw_retweet_process_msg)
        raw_remove_retweets()
    if input_option == 3:
        print(raw_csv_conversion_msg)
        raw_csv_conversion()
    if input_option == 0:
        print("Exit")
        start = False

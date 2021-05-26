import os
from dotenv import load_dotenv
from raw_processing.raw_utilities import raw_search_twitter, raw_remove_retweets, raw_csv_conversion
from data.database.raw.configuration import raw_build

load_dotenv()

topic = os.getenv("TAG") or "Football"
raw_search_msg = "Will takes some time. Searching for tweets with tag topic: {topic}".format(topic=topic)
raw_retweet_process_msg = "Raw data process initiated. Retweets to be removed."
raw_csv_conversion_msg = "Converting processed raw data, no retweets, into csv."

def options():
    print('\nRAW Data Options:\n')
    print('[1] Search twitter API for football topic')
    print('[2] Remove retweets and language filter from existing raw JSON data')
    print('[3] Convert processed raw data to CSV file')
    print('[4] Build Raw Database')
    print('\n[101] To reprint options')
    print('[0] To exit program')

options()
start = 1
while start == True:
    input_option = int(input('\nWhich option>'))
    if input_option == 101:
        # Reprints option selection
        options()
    if input_option == 1:
        # Initiates tweet search
        print(raw_search_msg)
        raw_search_twitter()
    if input_option == 2:
        # Initiates basic raw data processing
        print(raw_retweet_process_msg)
        raw_remove_retweets()
    if input_option == 3:
        # Converts raw data json to csv
        print(raw_csv_conversion_msg)
        raw_csv_conversion()
    if input_option == 4:
        # Creates database
        print("Building Raw Extraction Database")
        # Pass a true value to initiate raw_build order
        raw_build(1)
    if input_option == 0:
        # Exits program
        print("Exit")
        start = False
from resources import raw_search_msg, raw_retweet_process_msg, raw_csv_conversion_msg
from data.process.raw.utilities import raw_search_twitter, raw_remove_retweets, raw_csv_conversion

# Database configuration module
from data.database.raw.configuration import raw_build

# Database ETL utility module
from data.database.raw.utilities import load_raw_data

def options():
    """Function holding program option selections"""

    print('\nRAW Data Options:\n')
    print('[1] Search twitter API for football topic')
    print('[2] Remove retweets and language filter from existing raw JSON data')
    print('[3] Convert processed raw data to CSV file')
    print('[4] Build Raw Database')
    print('[5] Load processed data into database')
    print('\n[101] To reprint options')
    print('[0] To exit program')

# Initiate program option selection
options()

# Maintain option selection
start = 1
while start == True:
    input_option = int(input('\nWhich option > '))
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
        print("Building Raw Extraction Database.")
        # Pass a true value to initiate raw_build order
        raw_build(1)
    if input_option == 5:
        print("Loading raw processed data into Raw Extraction Database.")
        load_raw_data()
    if input_option == 0:
        # Exits program
        print("Exit")
        start = False
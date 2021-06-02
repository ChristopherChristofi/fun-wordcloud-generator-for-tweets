from resources import raw_search_msg, raw_retweet_process_msg, raw_csv_conversion_msg

# Data pre-processing modules
from process.raw.utilities import raw_search_twitter, raw_remove_retweets, raw_csv_conversion
from process.stage.process import commit_stage_processing

# Database configuration module
from database.raw.configuration import raw_build
from database.stage.configuration import stage_build
# Database ETL utility module
from database.raw.utilities import load_raw_data
from database.stage.utilities import load_stage_data

def options():
    """Function holding program option selections"""

    print('\nRAW Data Options:\n')
    print('[1] Search twitter API for football topic (replaces raw origin data)')
    print('[2] Remove retweets and filter language from existing raw JSONL data')
    print('[3] Convert processed raw JSONL data to CSV file')
    print('[4] Build Raw Database')
    print('[5] Load raw processed CSV data into database')
    print('\nSTAGE Data Options:\n')
    print('[6] View stage processing: type conversion, date refomatting, deduplication')
    print('[7] Convert processed data to CSV (Tweet, User, Date)')
    print('[8] Initiate NLP preprocess and csv conversion.')
    print('[9] Build Staging Database')
    print('[10] Load processed stage data into stage database')
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
        print("Initial raw data filter tranformation complete.")
    if input_option == 3:
        # Converts raw data json to csv
        print(raw_csv_conversion_msg)
        raw_csv_conversion()
        print("Raw data converted to CSV format")
    if input_option == 4:
        # Creates database
        print("Building Raw Extraction Database.")
        # Pass a true value to initiate raw_build order
        raw_build(1)
        print("Raw Database Built.")
    if input_option == 5:
        # Loads raw csv data into raw database
        print("Loading raw processed data into Raw Extraction Database.")
        load_raw_data()
        print("Raw data loaded.")
    if input_option == 6:
        print("Processing stage data.")
        commit_stage_processing(csv_convert=0, process=1)
    if input_option == 7:
        print("Converting processed stage data to CSV.")
        commit_stage_processing(csv_convert=1, process=1)
        print("Converted to CSV complete.")
    if input_option == 8:
        print("Initiating NLP processing.")
        commit_stage_processing(csv_convert=0, transformation=1, process=1)
        print("NLP complete.")
    if input_option == 9:
        # Creates database
        print("Building Stage Extraction Database.")
        # Pass a true value to initiate raw_build order
        stage_build(1)
    if input_option == 10:
        # Loads raw csv data into raw database
        print("Loading processed stage data into Stage Database.")
        load_stage_data()
        print("Stage data loaded.")

    if input_option == 0:
        # Exits program
        print("Exit")
        start = False
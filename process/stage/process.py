import petl as etl
import sqlite3
from data.resources import raw_database_path, raw_tablename
from process.stage.utilities import str_conversion, reformat_date, tweet_deduplicate

def stage_processing(table):

    """Function that preprocesses streamed data: converts id's to string from integer,
    reformats the data parameter, and ensures deduplication of tweet_id"""

    def id_processing(table):

        """Function that calls string conversion utility function"""

        conversion_table = str_conversion(table)

        print("ID data type (int => str) conversion complete.")

        return conversion_table


    def date_processing (table):

        """Function that calls date reformatting utility function"""

        date_table = reformat_date(table)

        print("Date reformatted")

        return date_table

    def deduplication_process (table):

        """Function that calls the deduplication utility function"""

        deduplicated_table = tweet_deduplicate(table)

        print("Deduplication complete. Tweet_id row copy removed.")

        return deduplicated_table

    table = id_processing(table)

    table = date_processing(table)

    table = deduplication_process(table)

    # row_count = etl.nrows(table)

    # print(row_count)

    print(table)

def commit_stage_processing(process=0):

    """Function that, when True, reconnects to the database and iniates the processing of
    the now staging data"""

    raw_db = raw_database_path
    raw_table = raw_tablename

    if process == True:

        conn = sqlite3.connect(raw_db)
        processing_table = etl.fromdb(conn, 'SELECT * FROM {table}'.format(table=raw_table))

        # row_count = etl.fromdb(conn, 'SELECT COUNT(id) FROM {table}'.format(table=raw_table))

        # print(row_count)

        stage_processing(processing_table)

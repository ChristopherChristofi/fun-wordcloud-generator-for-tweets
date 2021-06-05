import petl as etl
import sqlite3
from data.resources import raw_database_path, raw_tablename
from process.stage.utilities import str_conversion, reformat_date, tweet_deduplicate, integrate_staging_csv_conversion, tweet_text_lowercase
from process.stage.nlp import integrate_nlp_transformation

def stage_processing(csv_convert, transformation, table):

    """Function that preprocesses streamed data: converts id's to string from integer,
    reformats the data parameter, and ensures deduplication of tweet_id"""

    def id_processing(table):

        """Function that calls string conversion utility function"""

        conversion_table = str_conversion(table)

        return conversion_table


    def date_processing (table):

        """Function that calls date reformatting utility function"""

        date_table = reformat_date(table)

        return date_table

    def deduplication_process (table):

        """Function that calls the deduplication utility function"""

        deduplicated_table = tweet_deduplicate(table)

        return deduplicated_table

    def lowercasing_process (table):

        """"Function that calls the lowercasing utility function"""

        lower_table = tweet_text_lowercase(table)

        return lower_table

    table = id_processing(table)

    table = date_processing(table)

    table = deduplication_process(table)

    table = lowercasing_process(table)

    # row_count = etl.nrows(table)

    # print(row_count)

    print(table)

    if transformation == True:

        integrate_nlp_transformation(table)

    if csv_convert == True:

        integrate_staging_csv_conversion(table)

def commit_stage_processing(csv_convert=0, transformation=0, process=0):

    """Function that, when True, reconnects to the database and iniates the processing of
    raw staging data"""

    raw_db = raw_database_path
    raw_table = raw_tablename

    if process == True:

        conn = sqlite3.connect(raw_db)
        processing_table = etl.fromdb(conn, 'SELECT * FROM {table}'.format(table=raw_table))

        # row_count = etl.fromdb(conn, 'SELECT COUNT(id) FROM {table}'.format(table=raw_table))

        # print(row_count)

        stage_processing(csv_convert, transformation, processing_table)

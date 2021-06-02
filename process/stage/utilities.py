import arrow
import petl as etl
from data.resources import stage_tweet_csv, stage_date_csv, stage_user_csv

def format_date (date):

    """Function that utilies arrow package to yield transformed date property"""

    # format for raw tweet created_at date attribute:
    # "Mon Jan 01 23:59:59 +0000 2000"
    original_format = r"ddd[\s+]MMM[\s+]DD[\s+]HH:mm:ss[\s+]Z[\s+]YYYY"

    transformed_date = arrow.get(date, original_format).format('YYYY-MM-DD')

    return transformed_date

def reformat_date (table):

    """Function that parses the date column of input data table, conducting date
    format conversion through calling the formatting function"""

    date_table = etl.convert(table, 'tweet_date', lambda v: format_date(v))

    return date_table

def str_conversion (frame):

    """Function thats converts the int data type id's of specified columns to str"""

    conversion_table = etl.convert(frame, ('user_id', 'tweet_id'), str)

    return conversion_table

def tweet_deduplicate (frame):

    """Function that returns only the first row of a found duplicate concerning tweet_id"""

    deduplicated_table = etl.groupselectfirst(frame, key='tweet_id')

    return deduplicated_table

def tweet_text_lowercase (frame):

    """Function that converts all the str text in a column to lowercase"""

    lower_table = etl.convert(frame, 'tweet_text', 'lower')

    return lower_table

def stage_csv_conversion (data, path):

    """Function to convert processed to dataframe to CSV file."""

    etl.tocsv(data, path, encoding="utf8")

def cut_columns (frame, parameters):

    """Function to cut dataframe by input parameter column names."""

    cut_table = etl.cut(frame, [col for col in parameters])

    return cut_table

def integrate_staging_csv_conversion (frame):

    """Holds the nested functions that implement the transformation of the processed
    staged data table frame, before converting each processed data frame to CSV"""

    stage_csv_conversion(cut_columns(frame, ['tweet_id', 'tweet_text']), stage_tweet_csv)

    stage_csv_conversion(cut_columns(frame, ['user_id', 'tweet_id']), stage_user_csv)

    stage_csv_conversion(cut_columns(frame, ['tweet_date', 'tweet_id']), stage_date_csv)

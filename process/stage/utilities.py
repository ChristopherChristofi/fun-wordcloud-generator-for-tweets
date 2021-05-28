import arrow
import petl as etl

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

def cut_date (frame):

    """Not currently in use - seperates table"""

    cut_table = etl.cut(frame, 0, 'tweet_id', 'tweet_date')

    return cut_table

def str_conversion (frame):

    """Function thats converts the int data type id's of specified columns to str"""

    conversion_table = etl.convert(frame, ('user_id', 'tweet_id'), str)

    return conversion_table

def tweet_deduplicate (frame):

    """Function that returns only the first row of a found duplicate concerning tweet_id"""

    deduplicated_table = etl.groupselectfirst(frame, key='tweet_id')

    return deduplicated_table
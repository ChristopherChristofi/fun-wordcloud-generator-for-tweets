import psycopg2
import petl as etl
from data.resources import stage_db_name, stage_db_user, stage_db_pass
from data.resources import stage_tweet_csv, stage_user_csv, stage_date_csv
from data.resources import stage_tweet_table, stage_user_table, stage_date_table

def load_stage_data():
    """Function to load stage data into the configured stage database."""

    def extract_staging_csv(dataframe):
        """Nested function to load processed stage csv data to table data frame"""

        table = etl.fromcsv(dataframe, encoding='utf8')

        return table

    conn = psycopg2.connect(
        database=stage_db_name
        ,user=stage_db_user
        ,password=stage_db_pass
        )

    etl.todb(extract_staging_csv(stage_tweet_csv), conn, stage_tweet_table)

    etl.todb(extract_staging_csv(stage_user_csv), conn, stage_user_table)

    etl.todb(extract_staging_csv(stage_date_csv), conn, stage_date_table)
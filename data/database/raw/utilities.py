import petl as etl
import sqlite3
from data.resources import raw_csv_data, raw_datatable_headers, raw_database_path

def load_raw_data():
    """Function to load raw extracted data into the configured raw database."""

    def extract_raw_csv():
        """Nested function to load extracted raw processed csv data to table data frame"""

        table = etl.fromcsv(raw_csv_data, header=raw_datatable_headers, encoding='utf8')

        return table

    raw_data = extract_raw_csv()

    conn = sqlite3.connect(raw_database_path)

    etl.todb(raw_data, conn, 'rawtwittertweet')

    print("Data loaded.")


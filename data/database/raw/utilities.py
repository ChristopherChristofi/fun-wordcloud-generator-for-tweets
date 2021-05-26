import petl as etl
import csv
import sqlite3
from data.resources import raw_csv_data, raw_datatable_headers

def load_raw_data():

    def extract_raw_csv():
        table = etl.fromcsv(raw_csv_data, header=raw_datatable_headers)

        return table

    raw_data = extract_raw_csv()

    print(raw_data)


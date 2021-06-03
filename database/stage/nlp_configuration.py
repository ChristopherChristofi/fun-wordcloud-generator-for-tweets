from urllib.parse import quote_plus
from pymongo import MongoClient
from database.stage.utilities import load_nlp_stage_data
from data.resources import stage_mg_db_port, stage_mg_db_host, stage_mg_db_user, stage_mg_db_pass

user = stage_mg_db_user
password = stage_mg_db_pass
mongodbhost = stage_mg_db_host
port = stage_mg_db_port
host = "{host}:{port}".format(host=mongodbhost, port=port)

def mongodb_stage_build(run=0):
    """Function that initiates the build order of the NoSQL database for the stage datasets that are nlp processed and JSON format."""

    uri = "mongodb://%s:%s@%s" % (
        quote_plus(user), quote_plus(password), host
    )

    if run == True:
        client = MongoClient(uri)

        database = client.nlp_stage_database

        load_nlp_stage_data(database)
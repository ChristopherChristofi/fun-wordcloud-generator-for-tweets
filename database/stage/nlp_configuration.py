from urllib.parse import quote_plus
from pymongo import MongoClient
from database.stage.utilities import load_nlp_stage_data
from process.production.process import generate_wordcloud
from data.resources import stage_mg_db_port, stage_mg_db_host, stage_mg_db_user, stage_mg_db_pass

user = stage_mg_db_user
password = stage_mg_db_pass
mongodbhost = stage_mg_db_host
port = stage_mg_db_port
host = "{host}:{port}".format(host=mongodbhost, port=port)

def mongodb_stage_build(run=0, build=0, conn=0):
    """Function that initiates the build order of the NoSQL database for the stage datasets that are nlp processed and JSON format."""

    uri = "mongodb://%s:%s@%s" % (
        quote_plus(user), quote_plus(password), host
    )

    if run == True:
        # Run database processes if run is true
        client = MongoClient(uri)

        database = client.nlp_stage_database

        if build == True:
            # Initiate build methods if build call is true
            load_nlp_stage_data(database)

        if conn == True:
            # Initiate data loading and wordcloud generation.
            generate_wordcloud(database)



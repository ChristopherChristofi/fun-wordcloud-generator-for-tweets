from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from data.resources import raw_database_path_config, raw_tablename

raw_database = "sqlite:///{database}".format(
    database=raw_database_path_config
)

tablename = raw_tablename
Base = declarative_base()

class RawTwitterTweet(Base):
    __tablename__= tablename

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    tweet_id = Column(Integer)
    tweet_date = Column(String)
    tweet_text = Column(String)
    tweet_lang = Column(String)

def raw_build(run=0):
    """Function that initiates the build order of the database for raw datasets."""

    if run == True:
        engine = create_engine(raw_database)

        Base.metadata.create_all(engine)

        print("Database created.")
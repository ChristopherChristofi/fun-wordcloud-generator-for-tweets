from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from data.resources import raw_database_path_config

raw_database = "sqlite:///{database}".format(
    database=raw_database_path_config
)

Base = declarative_base()

class RawTwitterTweet(Base):
    __tablename__= 'rawtwittertweet'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    tweet_id = Column(Integer, nullable=False)
    tweet_date = Column(String(250), nullable=False)
    tweet_text = Column(String(250))
    tweet_lang = Column(String(250))

def raw_build(run=0):
    """Function that initiates the build order of the database for raw datasets."""

    if run == True:
        engine = create_engine(raw_database)

        Base.metadata.create_all(engine)

        print("Database created.")

raw_build()
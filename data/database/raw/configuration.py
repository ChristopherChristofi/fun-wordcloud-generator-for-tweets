from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from data.resources import raw_database_naming

raw_database_path = "sqlite:///data/database/raw/{database}".format(
    database=raw_database_naming
)

Base = declarative_base()

class RawTwitterTweet(Base):
    __tablename__= 'rawtwittertweet'

    id = Column(Integer, primary_key=True)
    tweet_date = Column(String(250), nullable=False)
    user = Column(Integer, nullable=False)
    tweet_id = Column(Integer, nullable=False)
    tweet_text = Column(String(250))
    tweet_lang = Column(String(250))

def raw_build(run=0):
    """Function that initiates the build order of the database for raw datasets."""

    if run == True:
        engine = create_engine(raw_database_path)

        Base.metadata.create_all(engine)

        print("Database created: {database}".format(
            database=raw_database_naming
            ))

raw_build()
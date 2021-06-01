from sqlalchemy import create_engine, Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import create_database, database_exists
from data.resources import stage_db_host, stage_db_port, stage_db_user, stage_db_pass, stage_date_table, stage_tweet_table, stage_user_table, stage_db_name

stage_database = "postgresql://{user}:{passw}@{host}:{port}/{database}".format(
    user=stage_db_user
    ,passw=stage_db_pass
    ,host=stage_db_host
    ,port=stage_db_port
    ,database=stage_db_name
)

Base = declarative_base()

class TwitterTweet(Base):
    __tablename__ = stage_tweet_table

    id = Column(Integer, primary_key=True)
    tweet_id = Column(String, unique=True)
    tweet_text = Column(String)
    date_made = relationship("TweetDate", uselist=False, back_populates="date_of_tweet")

    def __init__(self, tweet_id, tweet_text):
        self.tweet_id = tweet_id
        self.tweet_text = tweet_text

class TwitterUser(Base):
    __tablename__ = stage_user_table

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    tweet_id = Column(String, ForeignKey('{table}.tweet_id'.format(
        table=stage_tweet_table
    )))
    stage_tweet_table = relationship("TwitterTweet")

    def __init__(self, user_id):
        self.user_id = user_id

class TweetDate(Base):
    __tablename__ = stage_date_table

    id = Column(Integer, primary_key=True)
    tweet_date = Column(Date)
    tweet_id = Column(String, ForeignKey('{table}.tweet_id'.format(
        table=stage_tweet_table
    )))
    date_of_tweet = relationship("TwitterTweet", back_populates="date_made")

    def __init__(self, tweet_date):
        self.tweet_date = tweet_date

def stage_build(run=0):
    """Function that initiates the build order of the database for raw datasets."""

    if run == True:
        engine = create_engine(stage_database)
        if not database_exists(engine.url):
            create_database(engine.url)

        Base.metadata.create_all(engine)

        print("Database created.")
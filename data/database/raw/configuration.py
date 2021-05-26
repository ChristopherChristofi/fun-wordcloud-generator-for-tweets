from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from data.database.raw.resources import raw_database_naming

raw_database_path = "sqlite:///data/database/raw/{database}".format(
    database=raw_database_naming
)

Base = declarative_base()

class TwitterUser(Base):
    __tablename__ = 'twitteruser'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, nullable=False)

class TwitterTweet(Base):
    __tablename__ = 'twittertweet'

    id = Column(Integer, primary_key=True)
    tweet_id = Column(Integer, nullable=False)
    tweet_text = Column(String(250))
    user_id = Column(Integer, ForeignKey('twitteruser.user'))
    twitteruser = relationship(TwitterUser)

class TweetDate(Base):
    __tablename__ = 'tweetdate'

    id = Column(Integer, primary_key=True)
    tweet_date = Column(String(250), nullable=False)
    tweet_id = Column(Integer, ForeignKey('twittertweet.tweet_id'))
    twittertweet = relationship(TwitterTweet)

def raw_build(run=0):

    if run == True:
        engine = create_engine(raw_database_path)

        Base.metadata.create_all(engine)

        print("Database created: {database}".format(
            database=raw_database_naming
            ))

raw_build()
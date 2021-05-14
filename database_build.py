# Table creation sql instructions
build_commands = (# Table concerning twitterdetails for user
                '''CREATE TABLE IF NOT EXISTS twitter_users(user_id BIGINT PRIMARY KEY, user_name TEXT);''',
                # Table concernig tweet data
                '''CREATE TABLE IF NOT EXISTS user_tweets(tweet_id BIGINT PRIMARY KEY,
                                                    user_id BIGINT,
                                                    tweet TEXT,
                                                    retweet_count INT,
                                                    CONSTRAINT fk_tweet
                                                        FOREIGN KEY(user_id)
                                                            REFERENCES twitter_users(user_id));''',
                # Table concerning tweet entity relevant data
                '''CREATE TABLE IF NOT EXISTS tweet_entities(id SERIAL PRIMARY KEY,
                                                    tweet_id BIGINT,
                                                    hashtag TEXT,
                                                    CONSTRAINT fk_tweet
                                                        FOREIGN KEY(tweet_id)
                                                            REFERENCES user_tweets(tweet_id));'''
)
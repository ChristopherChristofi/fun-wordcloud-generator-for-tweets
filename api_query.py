import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from api_utilities import clean
from database_queries import queryCommand


# Call sql select query
stream_data = queryCommand("SELECT user_id, tweet_id, tweet FROM user_tweets;")

df_stream = pd.DataFrame(columns=['user_id','tweet_id','clean_tweet'])

for data in stream_data:
    index = len(df_stream)
    df_stream.loc[index,'user_id'] = data[0]
    df_stream.loc[index,'tweet_id'] = data[1]
    df_stream.loc[index,'clean_tweet'] = clean(data[2])

print(df_stream.head(20))

# Most commonly occuring words
def keywords():
    all_words = ' '.join([text for text in df_stream['clean_tweet']])
    wordcloud = WordCloud(width=800, height=500, random_state=21, max_font_size=110).generate(all_words)

    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

print(keywords())
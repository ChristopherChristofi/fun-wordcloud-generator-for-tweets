import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def integrate_data(data):

    """Funciton to generate wordcloud from input dataframe concerning NLP preprocessed tweet text"""

    tokens = ' '.join([token for token in data['tweet_text']])

    wordcloud = WordCloud(width=1000, height=700, random_state=21, max_font_size=110).generate(tokens)

    plt.figure(figsize=(10, 7))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()


def generate_wordcloud(db):

    """Function to extract the nlp processed data from the stage MongoDD database"""

    coll = db.nlp_stage_collection

    dataframe = pd.DataFrame(list(coll.find()))

    integrate_data(dataframe)
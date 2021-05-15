import re
from nltk.stem import WordNetLemmatizer

def clean(tweet):

    # Remove links characters
    tweet = re.sub(r'http\S+', '', tweet)
    # Remove characters suggestive of mentions
    tweet = re.sub('@\w+', '',tweet)
    # alphanumeric and hashtags
    tweet = re.sub('[^a-zA-Z#]', ' ',tweet)
    # remove multiple spaces and 
    tweet = re.sub('\s+', ' ',tweet)
    tweet = tweet.lower()
    # Use lemmatize method to further clean text
    lemmatizer = WordNetLemmatizer()
    sent = ' '.join([lemmatizer.lemmatize(w) for w in tweet.split() if len(lemmatizer.lemmatize(w))>3])

    return sent

def parse_hashtags(tags):
    '''Function thas parses streamed hashtags from retrieved entities'''

    hashtags = []

    for tag in tags:
        hashtags.append(tag['text'])
    return hashtags
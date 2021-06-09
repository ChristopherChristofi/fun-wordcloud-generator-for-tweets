import petl as etl
import re
from process.stage.utilities import cut_columns, stage_csv_conversion
from data.resources import stage_nlp_processed_csv
import nltk
from nltk.corpus import stopwords

def preprocessing_methods(data):

    """Main NLP preprocessing data pipeline to clean text data by defined methods."""

    def remove_hyperlinks(data):

        """Removes hyperink like texts."""

        processed_data = re.sub(r'http\S+', ' ', data)

        return processed_data

    def remove_mentions(data):

        """Removes twitter mentions and @ like tweet data strings."""

        processed_data = re.sub("@\w+"," ",data)

        return processed_data

    def remove_short_words(data):

        """Removes individual strings less than two characters long."""

        processed_data = re.sub(r'\s+\w{2}\s+', ' ', data)

        return processed_data

    def nlp_tokenization(data):

        """Function that tokensizers parsing text document into individual tokens."""

        tokens = nltk.word_tokenize(data)

        valid_tokens = [w for w in tokens if w.isalpha()]

        return valid_tokens

    def nlp_remove_stopwords(data):

        """Function to remove stopwords from input tweet text data"""

        stop_words = stopwords.words("english")

        # Example of further stopword additions to be removed
        stop_words = stop_words + ['back', 'actually', 'vs', 'might', 'gets', 'got', 'would']

        stop_words = set(stop_words)

        valid_tokens = [w for w in data if not w in stop_words]

        return valid_tokens

    data_1 = remove_hyperlinks(data)

    data_2 = remove_mentions(data_1)

    data_3 = remove_short_words(data_2)

    data_4 = nlp_tokenization(data_3)

    data_5 = nlp_remove_stopwords(data_4)

    return data_5

def stage_preprocessing(data):

    """Function that calls the nlp preprocessing data pipeline on the defined tweet_text parameter column."""

    # Preprocessing conversion of text column
    processed_data = etl.convert(data, 'tweet_text', lambda text: preprocessing_methods(text))

    return processed_data

def integrate_nlp_transformation(table):

    """Nested function to organise dataset and initiate NLP preprocessing."""

    # Prepare call csv conversion function
    stage_csv_conversion(
        # Initiate NLP preprocessing on given data frame
        stage_preprocessing(
            # Limit datafram by provided header parameters
            cut_columns(table, ['user_id', 'tweet_id', 'tweet_text'])
            )
            , stage_nlp_processed_csv
            )

import petl as etl
import re
from gensim.parsing.preprocessing import strip_multiple_whitespaces, preprocess_string, remove_stopwords, strip_numeric, strip_punctuation, strip_tags
from process.stage.utilities import cut_columns, stage_csv_conversion
from data.resources import stage_nlp_processed_csv

def preprocessing_methods(data):

    """Main NLP preprocessing function to clean text data by defined methods."""

    remove_links = lambda s: re.sub(r'http\S+', '', s)

    remove_mentions = lambda s: re.sub("@\w+","",s)

    lowercasing = lambda s: s.lower()

    remove_minimal_char_lengths = lambda s: re.sub(r'\s+\w{1}\s+', '', s)

    remove_alphanum_hashtags = lambda s: re.sub("[^a-zA-Z#]"," ",s)

    CUSTOM_FILTERS =    [strip_tags,
                        strip_numeric,
                        strip_punctuation,
                        strip_multiple_whitespaces,
                        remove_links,
                        remove_stopwords,
                        lowercasing,
                        remove_mentions,
                        remove_alphanum_hashtags,
                        remove_minimal_char_lengths]

    # Preprocessing conversion of text column
    processed_data = etl.convert(data, 'tweet_text', lambda text: preprocess_string(text, CUSTOM_FILTERS))

    return processed_data

def integrate_nlp_transformation(table):

    """Nested function to organise dataset and initiate NLP preprocessing."""

    # Prepare call csv conversion function
    stage_csv_conversion(
        # Initiate NLP preprocessing on given data frame
        preprocessing_methods(
            # Limit datafram by provided header parameters
            cut_columns(table, ['user_id', 'tweet_id', 'tweet_text'])
            )
            , stage_nlp_processed_csv
            )

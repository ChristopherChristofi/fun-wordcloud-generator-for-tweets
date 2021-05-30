import subprocess
from resources import topic
from data.resources import raw_searched_data, raw_processed_data, raw_csv_data

def raw_search_twitter():
    """Function that utilises twarc package to search twitter API for tweets."""

    search_twitter_cmd = "twarc search {topic} > {filename}".format(
        topic=topic
        ,filename=raw_searched_data
        )
    subprocess.run(
        search_twitter_cmd
        ,shell=True
        )

def raw_remove_retweets():
    """Function utilising the jq package to parse retrieved twitter data: removing retweets and non-english language tweets in bash environment."""

    raw_remove_retweet_cmd = """jq -r ' . | select(.retweeted_status == null) | select(.lang == "en")' {filename} > {output_file}""".format(
        filename=raw_searched_data
        ,output_file=raw_processed_data
        )
    cmd = "bash"
    subprocess.Popen([
        cmd
        ,"-c"
        ,raw_remove_retweet_cmd
    ])

def raw_csv_conversion():
    """Function that converts the processed data into a csv file in a bash environment."""

    # ".entities.hashtags[].text" to add hashtag entities, requiring 'join(";")', otherwise "," delimited
    raw_data_parameters = ".user.id, .id, .created_at, .full_text, .lang"
    raw_csv_conversion_cmd = """jq -r ' . | [{object}] |  @csv' {filename} > {output_file}""".format(
        object=raw_data_parameters
        ,filename=raw_processed_data
        ,output_file=raw_csv_data
        )
    cmd = "bash"
    subprocess.Popen([
        cmd
        ,"-c"
        ,raw_csv_conversion_cmd
    ])

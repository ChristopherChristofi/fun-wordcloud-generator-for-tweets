# football-team-NLP-tweet-analysis

## Description:

Simple program that interacts with the twitter API. Retrieved using the twarc package, tweets in raw format are processed in jq. TODO tweet data will be used to generate a wordcloud after natural language processing methods.

## Dependencies:

- petl
- arrow
- SQLAlchemy
- SQLAlchemy-Utils
- jq
- twarc
- psycopg2
- python-dotenv
- wordcloud
- gensim

## Build Instructions

(Some used scripts can be found in command_logs/)

1. **Install dependencies**
```sh
pip install -r requirements.txt
```

2. **Quick - Run program**

```sh
python main.py
```
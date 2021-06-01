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

## Build Instructions

Building in a Windows environment with WSL component. Create venv in both. (Some used scripts can be found
in command_logs/)

1. **Install dependencies in Windows environment**
```sh
pip install -r constraints.txt
```

2. **Install dependencies in WSL environment**
```sh
pip install -r requirements.txt
```

3. **Quick - Run program**

```sh
python main.py
```
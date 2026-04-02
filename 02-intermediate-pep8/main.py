"""Newsletter Analyzer System with multiple APIs."""

# Using "." to import from the news_analyzer package, to indicate that the module is part of the same package.
from news_analyzer.api_client import fetch_news
from news_analyzer.config import API_KEY
from news_analyzer.exceptions import APIKeyError

# Starting with response_data as None to ensure it is defined even if an exception occurs
response_data = None
try:
    response_data = fetch_news("newsapi", api_key=API_KEY, query="Python programming")
except APIKeyError as e:
    print(f"{e}")

# Checking if response_data is not None before trying to access its content
if response_data:
    for article in response_data["articles"]:
        print(article["title"])

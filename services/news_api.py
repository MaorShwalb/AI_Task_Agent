import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

    response = requests.get(url)
    articles = response.json().get("articles", [])

    return [a["title"] for a in articles[:5]]
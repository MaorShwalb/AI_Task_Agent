

import requests

API_KEY = "2b778f0f270e45eab20a6fd8baf0262c"

def get_news(query):
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={API_KEY}"

    response = requests.get(url)
    articles = response.json().get("articles", [])

    return [a["title"] for a in articles[:5]]
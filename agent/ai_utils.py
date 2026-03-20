import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

'''#for OpenAI model:
def summarize_news(news_list):
    if not news_list:
        return "No news to summarize."

    prompt = f"""
    Summarize the following financial news headlines into a short and clear summary:

    Headlines:
    {chr(10).join(news_list)}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )

    return response.choices[0].message.content'''

#default
def summarize_news(news_list):
    return "Mock summary: market news looks stable."
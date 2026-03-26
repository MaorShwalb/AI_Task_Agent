
#python -m pip install groq
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def summarize_news(news_list):
    print(">>> Calling Groq API...")

    news_text = "\n".join(news_list)

    prompt = f"""
    Summarize the following news clearly and concisely:

    {news_text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are an assistant that summarizes news."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content


def ask_groq(question):
    print(">>> Calling Groq API...")

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a smart assistant that answers questions clearly and accurately."},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content



'''
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#for OpenAI model:
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



'''#default
def summarize_news(news_list):
    return "Mock summary: market news looks stable."'''
from services.finance_api import get_stock_price
from services.news_api import get_news
from agent.ai_utils import summarize_news, ask_groq


def tool_get_price(task):
    return {
        "price_data": get_stock_price("QQQ")
    }


def tool_get_news(task):
    news = get_news("QQQ")
    summary = summarize_news(news)
    return {
        "news_data": {
            "news": news,
            "summary": summary
        }
    }


def tool_ai_chat(task):
    return {
        "ai_response": ask_groq(task)
    }


# Tool Registry
TOOLS = {
    "get_price": {
        "function": tool_get_price,
        "description": "Get current stock price including open, high, low, and close values"
    },
    "get_news": {
        "function": tool_get_news,
        "description": "Get latest news headlines about the stock and provide a summary"
    },
    "ai_chat": {
        "function": tool_ai_chat,
        "description": "Answer general questions or provide explanations using AI"
    }
}
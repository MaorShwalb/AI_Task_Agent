from services.finance_api import get_stock_price
from services.news_api import get_news
from agent.ai_utils import summarize_news, ask_groq
import re


# 🧠 מיפוי חברות → סימבולים
COMPANY_TO_SYMBOL = {
    "apple": "AAPL",
    "tesla": "TSLA",
    "nvidia": "NVDA",
    "microsoft": "MSFT",
    "amazon": "AMZN",
    "google": "GOOGL",
    "meta": "META",
    "s&p": "SPY",
    "s&p 500": "SPY",
    "sp500": "SPY",
    "spy": "SPY"
}


def extract_symbol(task, symbol):
    # אם קיבלנו symbol מה-planner → נשתמש בו
    if symbol:
        return symbol.upper()

    task_lower = task.lower()

    # חיפוש לפי מילון
    for company, sym in COMPANY_TO_SYMBOL.items():
        if company in task_lower:
            return sym

    # חיפוש symbol ישיר (למשל TSLA)
    match = re.search(r'\b[A-Z]{2,5}\b', task)
    if match:
        return match.group(0)

    return None


def tool_get_price(task, symbol=None):
    symbol = extract_symbol(task, symbol)

    if not symbol:
        return {
            "price_data": "No symbol found in task"
        }

    data = get_stock_price(symbol)

    if not data:
        return {
            "price_data": f"No price found for {symbol}"
        }

    return {
        "price_data": data
    }


def tool_get_news(task, symbol=None):
    symbol = extract_symbol(task, symbol)

    if not symbol:
        return {
            "news_data": "No symbol found in task"
        }

    query = f"{symbol} stock"

    news = get_news(query)

    if not news:
        return {
            "news_data": f"No news found for {symbol}"
        }

    summary = summarize_news(news)

    return {
        "news_data": {
            "symbol": symbol,
            "news": news,
            "summary": summary
        }
    }


def tool_ai_chat(task, symbol=None):
    return {
        "ai_response": ask_groq(task)
    }


# Tool Registry
TOOLS = {
    "get_price": {
        "function": tool_get_price,
        "description": "Get stock price. Args: symbol (e.g. AAPL, TSLA)"
    },
    "get_news": {
        "function": tool_get_news,
        "description": "Get latest news about a stock. Args: symbol"
    },
    "ai_chat": {
        "function": tool_ai_chat,
        "description": "Answer general questions"
    }
}
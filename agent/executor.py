
from services.finance_api import get_stock_price
from services.news_api import get_news
from agent.ai_utils import summarize_news

def execute(steps):
    results = {}

    for step in steps:
        if step == "get_price":
            results["price"] = get_stock_price("QQQ")

        elif step == "get_news":
            news = get_news("QQQ")
            results["news"] = news

            # הוספת סיכום AI
            results["news_summary"] = summarize_news(news)

    return results


'''from services.finance_api import get_stock_price
from services.news_api import get_news

def execute(steps):
    results = {}

    for step in steps:
        if step == "get_price":
            results["price"] = get_stock_price("QQQ")

        elif step == "get_news":
            results["news"] = get_news("QQQ")

    return results'''
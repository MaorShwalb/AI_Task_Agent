from services.finance_api import get_stock_price
from services.news_api import get_news

def execute(steps):
    results = {}

    for step in steps:
        if step == "get_price":
            results["price"] = get_stock_price("QQQ")

        elif step == "get_news":
            results["news"] = get_news("QQQ")

    return results
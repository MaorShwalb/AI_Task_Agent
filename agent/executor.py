
from agent.tools import TOOLS
def execute(steps, task):
    results = {}

    for step in steps:
        tool_function = TOOLS.get(step)

        if not tool_function:
            print(f"⚠️ Unknown tool: {step}")
            continue

        try:
            result = tool_function(task)

            # אם התוצאה היא dict → נמזג
            if isinstance(result, dict):
                results.update(result)
            else:
                results[step] = result

        except Exception as e:
            print(f"❌ Error in tool {step}: {e}")

    return results



#----------------------------------------------------------------------

'''from services.finance_api import get_stock_price
from services.news_api import get_news
from agent.ai_utils import summarize_news, ask_groq

def execute(steps, task):
    results = {}

    for step in steps:
        if step == "get_price":
            results["price"] = get_stock_price("QQQ")

        elif step == "get_news":
            news = get_news("QQQ")
            results["news"] = news
            results["news_summary"] = summarize_news(news)

        elif step == "ai_chat":
            results["ai_response"] = ask_groq(task)

    return results'''

#----------------------------------------------------------------------
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
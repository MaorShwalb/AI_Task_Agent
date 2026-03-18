"""from services.finance_api import get_stock_price
from services.news_api import get_news

data = get_stock_price("QQQ")
news = get_news("QQQ")

print("Price:", data)
print("News:", news)
"""

from agent.planner import plan
from agent.executor import execute

task = "Get QQQ price and news"

steps = plan(task)
results = execute(steps)

print("Task:", task)
print("Results:", results)


from agent.planner import plan
from agent.executor import execute

#option: Get QQQ price and news
task = "Get QQQ price and news"

steps = plan(task)
results = execute(steps, task)

print("Task:", task)
print("Results:", results)

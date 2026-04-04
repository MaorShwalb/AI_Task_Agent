

from agent.planner import plan
from agent.executor import execute
from pprint import pprint #for lines prints

'''option: Get QQQ price and news
           Tell me what's happening with tech stocks
           
           task = "What's happening with Nvidia stock?"
            task = "Tell me about Apple"
            task = "TSLA news"
            task = "What's up with Microsoft stock?"
           
           '''
task = "tell me about s&p news"

steps = plan(task)
results = execute(steps, task)

print("Task:", task)
#print("Results:", results)

#print(results["news_summary"].replace("\\n", "\n")) #dont print prices need to check

pprint(results)

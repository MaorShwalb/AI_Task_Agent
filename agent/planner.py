
from agent.ai_utils import ask_groq
import json
import re

'''was: User → Code (if rules) → Steps → Execute
   now its: User → AI (LLM) → Steps → Execute'''
def extract_json(text):
    """Extract JSON array from LLM response"""
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return match.group(0)
    return None


def plan(task):
    prompt = f"""
    You are an AI planner.

    Your job is to break down a user request into steps.

    Available tools:
    - get_price → get stock price
    - get_news → get latest news
    - ai_chat → general AI response

    Rules:
    - Return ONLY a JSON array
    - Do NOT explain anything
    - Example output: ["get_price", "get_news"]

    Task: {task}
    """

    response = ask_groq(prompt)

    try:
        json_text = extract_json(response)

        if not json_text:
            raise ValueError("No JSON found")

        steps = json.loads(json_text)
        return steps

    except Exception as e:
        print("⚠️ Failed to parse LLM response:", response)
        return []


'''def plan(task):
    """
    מקבל מחרוזת משימה ומחזיר רשימת צעדים
    """
    steps = []
    task_lower = task.lower()

    if "price" in task_lower or "qqq" in task_lower:
        steps.append("get_price")

    if "news" in task_lower:
        steps.append("get_news")

    if "summarize" in task_lower or "explain" in task_lower:
        steps.append("ai_chat")

    return steps'''
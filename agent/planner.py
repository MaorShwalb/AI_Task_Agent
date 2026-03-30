
from agent.ai_utils import ask_groq
from agent.tools import TOOLS
import json
import re


def extract_json(text):
    match = re.search(r'\[.*\]', text, re.DOTALL)
    if match:
        return match.group(0)
    return None


def build_tools_description():
    """
    Build tools description dynamically from TOOLS registry
    """
    description = ""

    for name, tool_data in TOOLS.items():
        description += f"- {name}: {tool_data['description']}\n"

    return description


def plan(task):
    tools_description = build_tools_description()

    prompt = f"""
    You are an AI agent planner.

    Your job is to decide which tools to use to complete a task.

    Available tools:
    {tools_description}

    Rules:
    - Return ONLY a JSON array
    - Do NOT explain anything
    - Use only the tools listed above

    Example:
    Task: Get QQQ price and news
    Output: ["get_price", "get_news"]

    Task: {task}
    """

    response = ask_groq(prompt)

    try:
        json_text = extract_json(response)

        if not json_text:
            raise ValueError("No JSON found")

        steps = json.loads(json_text)
        return steps

    except Exception:
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
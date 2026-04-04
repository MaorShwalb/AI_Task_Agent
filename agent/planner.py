
from agent.ai_utils import ask_groq
from agent.tools import TOOLS
import json
import re


def extract_json(text):
    matches = re.findall(r'\[.*?\]', text, re.DOTALL)
    if matches:
        return matches[-1]  # לוקח את האחרון בלבד

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
    
    Your job is to decide which tools to use and with what arguments.
    
    Available tools:
    {tools_description}
    
    Rules:
    - Return ONLY a JSON array
    - Each step must include:
      - tool
      - args (dictionary)
    - Use only the tools listed above
    - Do NOT explain anything
    
    IMPORTANT:
    - If the task is about a stock or company (like Tesla, Nvidia, Apple):
      ALWAYS use:
      1. get_price
      2. get_news
    - Do NOT use ai_chat for stock analysis if data tools are available
    
    Example:
    Task: What's happening with Tesla stock?
    Output:
    [
      {{"tool": "get_price", "args": {{"symbol": "TSLA"}}}},
      {{"tool": "get_news", "args": {{"symbol": "TSLA"}}}}
    ]
    
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
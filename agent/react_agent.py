from agent.tools import TOOLS
from agent.ai_utils import ask_groq
from agent.memory import (
    add_user_message,
    add_assistant_message,
    get_conversation_text,
    update_symbols,
    get_last_symbols
)
import json
import re


def build_tools_description():
    description = ""
    for name, tool in TOOLS.items():
        description += f"{name}: {tool['description']}\n"
    return description


def parse_response(response):
    action_match = re.search(r"Action:\s*(\w+)", response)
    input_match = re.search(r"Action Input:\s*(\{.*\})", response, re.DOTALL)

    if not action_match or not input_match:
        raise ValueError("Invalid response format from LLM")

    action = action_match.group(1)

    try:
        args = json.loads(input_match.group(1))
    except:
        args = {}

    return action, args


def normalize_args(args):
    """
    מתקן טעויות נפוצות של ה-LLM
    """
    if not isinstance(args, dict):
        return {}

    # 🔧 symbols → symbol
    if "symbols" in args and "symbol" not in args:
        args["symbol"] = args.pop("symbols")

    # 🔧 stock_name → symbol
    if "stock_name" in args and "symbol" not in args:
        args["symbol"] = args.pop("stock_name")

    # 🔧 symbol קטן → גדול
    if "symbol" in args:
        if isinstance(args["symbol"], list):
            args["symbol"] = [s.upper() for s in args["symbol"]]
        elif isinstance(args["symbol"], str):
            args["symbol"] = args["symbol"].upper()

    return args


def run_react_agent(task, max_steps=5):
    add_user_message(task)

    history = ""
    tools_description = build_tools_description()

    for step in range(max_steps):
        print(f"\n--- Step {step+1} ---")

        conversation = get_conversation_text()
        last_symbols = get_last_symbols()

        prompt = f"""
        You are a smart AI agent that can think step-by-step.
        
        You have access to the following tools:
        
        {tools_description}
        
        IMPORTANT:
        - Use EXACT argument names
        - Do NOT invent parameters
        - If multiple stocks are requested, you may pass a list of symbols
        - Do NOT call the same tool twice with the same arguments
        
        CRITICAL RULES:
        - You MUST base your final answer ONLY on Observation data
        - If Observation is missing → DO NOT finish
        - If you finish without using Observation → your answer is WRONG
        - ALWAYS extract exact values from Observation (numbers, prices, etc.)
        - NEVER guess or invent values
        - You MUST copy exact values from Observation
        
        Recent symbols mentioned:
        {last_symbols}
        
        You MUST follow this format EXACTLY:
        
        Thought: ...
        Action: tool_name OR finish
        Action Input: JSON dictionary
        
        If you finish:
        Action: finish
        Action Input: {{"answer": "your final answer with real numbers"}}
        
        ---
        
        Conversation:
        {conversation}
        
        Current task:
        {task}
        
        Previous steps:
        {history}
        """

        response = ask_groq(prompt)
        print(response)

        # =========================
        # 🔚 finish
        # =========================
        if "Action: finish" in response:
            try:
                parts = response.split("Action Input:")

                if len(parts) < 2:
                    return "Failed to find Action Input."

                json_part = parts[-1].strip()

                answer_json = json.loads(json_part)

                final_answer = answer_json.get("answer", None)

                if not final_answer:
                    return f"Could not find 'answer' field in: {answer_json}"

                add_assistant_message(final_answer)
                return final_answer

            except Exception as e:
                return f"Final parsing error: {e}\nRaw: {response}"

        # =========================
        # 🔍 parse
        # =========================
        try:
            action, args = parse_response(response)
        except Exception as e:
            return f"Parsing error: {e}"

        # =========================
        # ⚙️ tool execution
        # =========================
        if action not in TOOLS:
            observation = f"Invalid tool: {action}"
        else:
            try:
                if "symbol" in args and isinstance(args["symbol"], list):
                    results = {}

                    for sym in args["symbol"]:
                        single_result = TOOLS[action]["function"](task, symbol=sym)
                        results[sym] = single_result
                        update_symbols(sym)

                    observation = json.dumps(results, indent=2)

                else:
                    result = TOOLS[action]["function"](task, **args)
                    observation = json.dumps(result, indent=2)

                    if "symbol" in args:
                        update_symbols(args["symbol"])

            except Exception as e:
                observation = f"Error: {str(e)}"

        # =========================
        # 🧠 update history
        # =========================
        history += f"""
{response}

Observation:
{observation}
"""

    return "Max steps reached without finishing."
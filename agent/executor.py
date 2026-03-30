
from agent.tools import TOOLS

def execute(steps, task):
    results = {}

    for step in steps:
        tool_data = TOOLS.get(step)

        if not tool_data:
            print(f"⚠️ Unknown tool: {step}")
            continue

        tool_function = tool_data["function"]

        try:
            result = tool_function(task)

            if isinstance(result, dict):
                results.update(result)
            else:
                results[step] = result

        except Exception as e:
            print(f"❌ Error in tool {step}: {e}")

    return results

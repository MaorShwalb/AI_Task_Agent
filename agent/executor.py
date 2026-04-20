
'''from agent.tools import TOOLS

def execute(steps, task):
    results = {}

    for step in steps:
        # נשלוף שם tool והפרמטרים
        tool_name = step.get("tool")
        args = step.get("args", {})

        tool_data = TOOLS.get(tool_name)

        if not tool_data:
            print(f"⚠️ Unknown tool: {tool_name}")
            continue

        tool_function = tool_data["function"]

        try:
            # העברת args דינמית
            result = tool_function(task, **args)

            if isinstance(result, dict):
                results.update(result)
            else:
                results[tool_name] = result

        except Exception as e:
            print(f"❌ Error in tool {tool_name}: {e}")

    return results'''
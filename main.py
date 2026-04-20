from agent.react_agent import run_react_agent

while True:
    task = input("\nYou: ")

    if task.lower() in ["exit", "quit"]:
        break

    result = run_react_agent(task)

    print("\nAgent:")
    print(result)
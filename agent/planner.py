def plan(task):
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

    return steps
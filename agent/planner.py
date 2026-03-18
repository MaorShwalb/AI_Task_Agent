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

    return steps
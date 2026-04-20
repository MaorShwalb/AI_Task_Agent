conversation_history = []
last_symbols = []  # 🆕 שומר מניות אחרונות


def add_user_message(message):
    conversation_history.append({
        "role": "user",
        "content": message
    })


def add_assistant_message(message):
    conversation_history.append({
        "role": "assistant",
        "content": message
    })


def get_conversation_text():
    history_text = ""

    for msg in conversation_history:
        role = msg["role"]
        content = msg["content"]

        history_text += f"{role.upper()}: {content}\n"

    return history_text


# 🆕 שומרים symbols
def update_symbols(symbol):
    if symbol and symbol not in last_symbols:
        last_symbols.append(symbol)

    # נשמור רק 3 אחרונים
    if len(last_symbols) > 3:
        last_symbols.pop(0)


def get_last_symbols():
    return last_symbols
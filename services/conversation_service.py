from database.conversations import (
    save_conversation,
    get_recent_conversations
)


def add(role, message):
    save_conversation(role, message)


def history(limit=10):
    return get_recent_conversations(limit)
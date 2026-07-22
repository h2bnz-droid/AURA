from database.connection import get_connection
from database.conversations import (
    save_conversation,
    get_recent_conversations,
    clear_conversations
)

def add(role: str, message: str):
    save_conversation(role, message)


def history(limit: int = 10):
    return get_recent_conversations(limit)

def clear_history():
    clear_conversations()
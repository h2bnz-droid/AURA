from database.memories import (
    save_memory,
    get_memory,
    get_all_memories,
    search_memories
)


def reminders():

    memories = get_all_memories()

    return [
        m for m in memories
        if m["category"] == "reminder"
    ]

def search(keyword):
    return search_memories(keyword)

def remember(category: str, key: str, value: str):
    """
    Menyimpan sebuah memori ke database.
    """
    save_memory(category, key, value)


def recall(key: str):
    """
    Mengambil memori berdasarkan key.
    """
    row = get_memory(key)

    if row is None:
        return None

    return row["memory_value"]

def recall_all():

    memories = get_all_memories()

    if not memories:
        return "Aku belum memiliki memori apa pun."

    result = []

    for memory in memories:
        result.append(f"• {memory['memory_value']}")

    return "\n".join(result)
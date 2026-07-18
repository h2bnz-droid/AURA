import ollama

from core.config import MODEL


def chat(messages):
    response = ollama.chat(
        model=MODEL,
        messages=messages
    )

    return response["message"]["content"]
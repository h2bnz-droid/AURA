import ollama
from core.personality import SYSTEM_PROMPT


def ask(user_message):

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response["message"]["content"]
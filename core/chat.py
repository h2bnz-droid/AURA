from core.personality import SYSTEM_PROMPT
from core.context_builder import build_context
from core.ai_provider import chat

from services.conversation_service import add


def ask(user_message: str):

    context = build_context(user_message)

    add("User", user_message)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": context
        }
    ]

    answer = chat(messages)

    add("AURA", answer)

    return answer
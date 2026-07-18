from core.prompt_builder import PromptBuilder
from core.personality import SYSTEM_PROMPT
from core.context_builder import build_context
from core.ai_provider import chat

from services.conversation_service import add


builder = PromptBuilder()


def ask(user_message: str):

    # Simpan pesan pengguna
    add("User", user_message)

    # Bangun context
    context = build_context(user_message)

    # Ubah context menjadi prompt
    prompt = builder.build(context)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    answer = chat(messages)

    # Simpan jawaban AURA
    add("AURA", answer)

    return answer
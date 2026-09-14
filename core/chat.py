from core.prompt_builder import PromptBuilder
from core.personality import SYSTEM_PROMPT
from core.context_builder import build_context
from core.ai_provider import chat
from core.security import (
    redact_sensitive_data,
    validate_user_input,
)

from services.conversation_service import add


builder = PromptBuilder()


def ask(user_message: str):

    # Validasi dan sanitasi pesan pengguna
    user_message = validate_user_input(user_message)
    safe_user_message = redact_sensitive_data(user_message)

    # Simpan pesan pengguna yang sudah disanitasi
    add("User", safe_user_message)

    # Bangun context
    context = build_context(safe_user_message)

    # Ubah context menjadi prompt
    prompt = builder.build(context)

    from core.config import DEBUG_PROMPT

    if DEBUG_PROMPT:
        safe_prompt = redact_sensitive_data(prompt)

        print("\n" + "=" * 60)
        print("PROMPT DEBUG")
        print("=" * 60)
        print(
            "Prompt berhasil dibuat. "
            f"Panjang prompt: {len(safe_prompt)} karakter."
        )
        print(
            "Isi prompt tidak ditampilkan untuk menjaga privasi."
        )
        print("=" * 60)

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": prompt,
        },
    ]

    answer = chat(messages)

    # Simpan jawaban AURA
    add("AURA", answer)

    return answer
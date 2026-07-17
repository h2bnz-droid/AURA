import ollama
from core.personality import SYSTEM_PROMPT

print("=" * 50)
print("        AURA v0.0.1 - Genesis")
print("=" * 50)

while True:

    user = input("\nAnda : ")

    if user.lower() in ["exit", "quit", "keluar"]:
        print("\nAURA : Sampai jumpa 😊")
        break

    response = ollama.chat(
        model="gemma3:1b",   # sesuaikan jika nama model berbeda
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user}
        ]
    )

    print("\nAURA :", response["message"]["content"])
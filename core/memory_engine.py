from typing import Optional

def process_memory(text: str) -> Optional[dict]:

    text = text.strip()

    lower = text.lower()

    triggers = [
        "ingat bahwa",
        "ingat",
        "catat",
        "tolong ingat",
        "jangan lupa"
    ]

    for trigger in triggers:

        if lower.startswith(trigger):

            content = text[len(trigger):].strip()

            if content:

                return {
                    "category": "note",
                    "key": "manual_note",
                    "value": content
                }

    return None
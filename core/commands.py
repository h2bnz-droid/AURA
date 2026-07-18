def detect_command(text):

    text = text.lower()

    if "siapa saya" in text:
        return "who_am_i"

    if "apa yang kamu ingat" in text:
        return "show_memory"

    return None
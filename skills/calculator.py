def execute(text):

    try:

        expression = (
            text.lower()
            .replace("hitung", "")
            .strip()
        )

        result = eval(expression)

        return f"Hasilnya adalah {result}"

    except Exception:
        return None
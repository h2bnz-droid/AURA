from core.engines.engine_manager import EngineManager


def run():

    manager = EngineManager()

    tests = [
        "Namaku Hiban",
        "Ingat bahwa aku suka matcha",
        "Aku ingin belajar Python",
        "Apa itu cyber security?"
    ]

    print("=== Engine Manager ===")

    for message in tests:

        print(f"\nUser : {message}")

        result = manager.process(message)

        if result:
            print(f"AURA : {result}")
        else:
            print("AURA : diteruskan ke AI")


if __name__ == "__main__":
    run()
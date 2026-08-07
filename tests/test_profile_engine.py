from core.engines.profile_engine import ProfileEngine


def run():

    engine = ProfileEngine()

    print("=== Profile Engine ===")

    print(
        engine.process("Namaku Hiban")
    )


if __name__ == "__main__":
    run()
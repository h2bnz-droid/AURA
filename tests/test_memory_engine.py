from core.engines.memory_engine import MemoryEngine


def run():

    engine = MemoryEngine()

    print("=== Memory Engine ===")

    print(
        engine.process(
            "Ingat bahwa warna favoritku biru"
        )
    )


if __name__ == "__main__":
    run()
from core.engines.goal_engine import GoalEngine


def run():

    engine = GoalEngine()

    print("=== Goal Engine ===")

    print(
        engine.process(
            "Aku ingin belajar Python"
        )
    )


if __name__ == "__main__":
    run()
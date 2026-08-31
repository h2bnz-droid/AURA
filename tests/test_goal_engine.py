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

from core.engines.goal_engine import GoalEngine


def run():

    engine = GoalEngine()

    print("=== Goal Engine ===")

    print(
        engine.process(
            "Aku ingin belajar Python"
        )
    )


def test_parse_progress_with_goal_prefix():
    engine = GoalEngine()

    result = engine._parse_progress(
        "progress goal belajar Python 50%"
    )

    assert result == ("belajar Python", 50)


def test_parse_progress_without_goal_prefix():
    engine = GoalEngine()

    result = engine._parse_progress(
        "progress belajar Python 50%"
    )

    assert result == ("belajar Python", 50)


def test_parse_progress_update_with_menjadi():
    engine = GoalEngine()

    result = engine._parse_progress(
        "update goal belajar Python menjadi 75%"
    )

    assert result == ("belajar Python", 75)


def test_parse_progress_invalid_percentage():
    engine = GoalEngine()

    assert engine._parse_progress(
        "progress goal belajar Python 101%"
    ) is None


if __name__ == "__main__":
    run()    
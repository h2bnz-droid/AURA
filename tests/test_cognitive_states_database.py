from database import cognitive_states


def test_create_cognitive_state_table():
    cognitive_states.create_table()


def test_save_and_get_latest_state():
    cognitive_states.create_table()

    cognitive_states.save_state(
        state_type="mindset",
        value="growth",
        confidence=1.0,
        source="test",
    )

    result = cognitive_states.get_latest_state("mindset")

    assert result is not None
    assert result["state_type"] == "mindset"
    assert result["value"] == "growth"
    assert result["confidence"] == 1.0
    assert result["source"] == "test"


def test_get_cognitive_state_history():
    cognitive_states.create_table()

    cognitive_states.save_state(
        state_type="mindset",
        value="resilient",
        confidence=0.9,
        source="test",
    )

    history = cognitive_states.get_state_history(
        state_type="mindset"
    )

    assert len(history) >= 1
    assert history[0]["state_type"] == "mindset"
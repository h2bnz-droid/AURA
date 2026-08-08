from unittest.mock import patch

from core.domain.planner_intent import PlannerIntent
from core.engines.planner_engine import PlannerEngine


def test_analyze_create_plan():
    engine = PlannerEngine()

    result = engine.analyze("buat rencana untuk belajar Python")

    assert result == PlannerIntent.CREATE_PLAN


def test_analyze_unknown():
    engine = PlannerEngine()

    result = engine.analyze("halo AURA")

    assert result == PlannerIntent.UNKNOWN


def test_extract_goal():
    engine = PlannerEngine()

    result = engine.extract_goal("buat rencana untuk belajar Python")

    assert result == "belajar Python"


def test_extract_goal_returns_none_for_unknown_prefix():
    engine = PlannerEngine()

    result = engine.extract_goal("halo AURA")

    assert result is None


def test_validate_goal():
    engine = PlannerEngine()

    assert engine.validate_goal("belajar Python") is True
    assert engine.validate_goal("ab") is False
    assert engine.validate_goal("") is False
    assert engine.validate_goal(None) is False


def test_generate_plan():
    engine = PlannerEngine()

    plan = engine.generate_plan("belajar Python")

    assert isinstance(plan, list)
    assert len(plan) == 3
    assert all(isinstance(step, str) for step in plan)


def test_process_create_plan():
    engine = PlannerEngine()

    with patch(
        "core.engines.planner_engine.save_plan"
    ) as mock_save_plan:
        result = engine.process(
            "buat rencana untuk belajar Python"
        )

    mock_save_plan.assert_called_once_with(
        "belajar Python",
        [
            "Langkah pertama",
            "Langkah kedua",
            "Langkah ketiga",
        ],
    )

    assert result is not None
    assert "belajar Python" in result
    assert "1. Langkah pertama" in result
    assert "2. Langkah kedua" in result
    assert "3. Langkah ketiga" in result


def test_process_unknown_returns_none():
    engine = PlannerEngine()

    result = engine.process("halo AURA")

    assert result is None


def test_process_invalid_goal():
    engine = PlannerEngine()

    result = engine.process("buat rencana untuk ab")

    assert result == (
        "Tujuan yang diberikan tidak valid."
        " Silakan berikan tujuan yang lebih jelas."
    )
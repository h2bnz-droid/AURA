from unittest.mock import patch

from services.planner_service import save_plan, all_plans


def test_save_plan():
    goal = "Belajar Python"
    steps = [
        "Pelajari dasar Python",
        "Buat project kecil",
        "Latihan setiap hari",
    ]

    with patch(
        "services.planner_service.create_plan"
    ) as mock_create_plan:
        save_plan(goal, steps)

    mock_create_plan.assert_called_once()

    args = mock_create_plan.call_args.args

    assert args[0] == goal
    assert args[1] == (
        '["Pelajari dasar Python", '
        '"Buat project kecil", '
        '"Latihan setiap hari"]'
    )
    assert args[2] == "active"
    assert args[3] == args[4]


def test_all_plans():
    expected_plans = [
        {
            "id": 1,
            "goal": "Belajar Python",
            "steps": '["Langkah pertama"]',
            "status": "active",
        }
    ]

    with patch(
        "services.planner_service.get_plans",
        return_value=expected_plans,
    ) as mock_get_plans:
        result = all_plans()

    mock_get_plans.assert_called_once()
    assert result == expected_plans
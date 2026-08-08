from core.engines.planner_engine import PlannerEngine
from services.planner_service import all_plans
from database.plans import create_table


def test_planner_full_flow():
    create_table()

    engine = PlannerEngine()

    result = engine.process(
        "buat rencana untuk belajar Python"
    )

    assert result is not None
    assert "belajar Python" in result

    plans = all_plans()

    assert plans

    latest_plan = plans[0]

    assert latest_plan["goal"] == "belajar Python"
    assert latest_plan["status"] == "active"
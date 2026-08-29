from core.engines.engine_manager import EngineManager


def test_planner_engine_integration():
    manager = EngineManager()

    result = manager.process("buat rencana untuk belajar Python")

    assert result is not None


def test_decision_engine_integration():
    manager = EngineManager()

    result = manager.process("bandingkan laptop A dan laptop B")

    assert result is not None


def test_knowledge_engine_integration():
    manager = EngineManager()

    result = manager.process("cari informasi tentang Python")

    assert result is not None


def test_conversation_engine_fallback():
    manager = EngineManager()

    result = manager.process("hari ini aku merasa produktif")

    assert result is not None


def test_unknown_message():
    manager = EngineManager()

    result = manager.process("")

    assert result is None

def test_process_passes_context_to_context_aware_engine():
    manager = EngineManager()

    class ContextAwareEngine:
        def process(self, message):
            return None

        def process_with_context(self, message, context):
            return f"{message}:{context}"

    manager.engines = [ContextAwareEngine()]

    context = {"response_style": "casual"}

    result = manager.process(
        "halo",
        context,
    )

    assert result == "halo:{'response_style': 'casual'}" 

def test_process_keeps_existing_engine_contract():
    manager = EngineManager()

    class LegacyEngine:
        def process(self, message):
            return f"legacy:{message}"

    manager.engines = [LegacyEngine()]

    result = manager.process(
        "halo",
        {"response_style": "casual"},
    )

    assert result == "legacy:halo"       
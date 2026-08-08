from core.domain.conversation_intent import ConversationIntent
from core.engines.conversation_engine import ConversationEngine


def test_analyze_greeting():
    engine = ConversationEngine()

    result = engine.analyze("halo AURA")

    assert result == ConversationIntent.GREETING


def test_analyze_greeting_variation():
    engine = ConversationEngine()

    result = engine.analyze("selamat pagi AURA")

    assert result == ConversationIntent.GREETING


def test_analyze_chat():
    engine = ConversationEngine()

    result = engine.analyze(
        "hari ini aku sedang merasa cukup produktif"
    )

    assert result == ConversationIntent.CHAT


def test_analyze_unknown_empty_message():
    engine = ConversationEngine()

    result = engine.analyze("")

    assert result == ConversationIntent.UNKNOWN


def test_analyze_whitespace_message():
    engine = ConversationEngine()

    result = engine.analyze("   ")

    assert result == ConversationIntent.UNKNOWN


def test_process_greeting():
    engine = ConversationEngine()

    result = engine.process("halo AURA")

    assert result is not None
    assert "Halo" in result


def test_process_chat():
    engine = ConversationEngine()

    result = engine.process(
        "hari ini aku sedang merasa cukup produktif"
    )

    assert result is not None
    assert "mendengarkan" in result


def test_process_empty_message():
    engine = ConversationEngine()

    result = engine.process("")

    assert result is None
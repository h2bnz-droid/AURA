from core.domain.knowledge_intent import KnowledgeIntent
from core.engines.knowledge_engine import KnowledgeEngine


def test_analyze_search():
    engine = KnowledgeEngine()

    result = engine.analyze(
        "cari informasi tentang Python"
    )

    assert result == KnowledgeIntent.SEARCH


def test_analyze_explain():
    engine = KnowledgeEngine()

    result = engine.analyze(
        "jelaskan Python"
    )

    assert result == KnowledgeIntent.EXPLAIN


def test_analyze_unknown():
    engine = KnowledgeEngine()

    result = engine.analyze(
        "ingat bahwa aku suka kopi"
    )

    assert result == KnowledgeIntent.UNKNOWN


def test_extract_search_query():
    engine = KnowledgeEngine()

    query = engine.extract_query(
        "cari informasi tentang Python"
    )

    assert query == "Python"


def test_extract_explain_query():
    engine = KnowledgeEngine()

    query = engine.extract_query(
        "jelaskan Python"
    )

    assert query == "Python"


def test_extract_query_unknown():
    engine = KnowledgeEngine()

    query = engine.extract_query(
        "halo AURA"
    )

    assert query is None


def test_validate_query():
    engine = KnowledgeEngine()

    assert engine.validate_query("Python")


def test_validate_invalid_query():
    engine = KnowledgeEngine()

    assert not engine.validate_query(None)
    assert not engine.validate_query("")
    assert not engine.validate_query("ab")


def test_process_search():
    engine = KnowledgeEngine()

    result = engine.process(
        "cari informasi tentang Python"
    )

    assert result is not None
    assert "Python" in result


def test_process_explain():
    engine = KnowledgeEngine()

    result = engine.process(
        "jelaskan Python"
    )

    assert result is not None
    assert "Python" in result


def test_process_invalid_query():
    engine = KnowledgeEngine()

    result = engine.process(
        "jelaskan ab"
    )

    assert result is not None
    assert "lebih jelas" in result


def test_process_unknown():
    engine = KnowledgeEngine()

    result = engine.process(
        "halo AURA"
    )

    assert result is None
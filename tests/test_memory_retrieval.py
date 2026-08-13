from unittest.mock import patch
from core.memory_retrieval import MemoryRetrieval
from core.context_builder import build_context


@patch("core.context_builder.history")
@patch("core.memory_retrieval.search")
@patch("core.context_builder.owner_name")
def test_retrieval_finds_relevant_memory(
    mock_owner_name,
    mock_search,
    mock_history,
):
    mock_owner_name.return_value = "Hibban"
    mock_history.return_value = []

    mock_search.side_effect = lambda word: {
        "python": [
            {
                "memory_value": "User sedang belajar Python"
            }
        ],
        "aura": [
            {
                "memory_value": "User sedang membangun AURA"
            }
        ],
    }.get(word, [])

    context = build_context(
        "Aku sedang belajar Python untuk membangun AURA"
    )

    values = [
        memory["memory_value"]
        for memory in context.memories
    ]

    assert "User sedang belajar Python" in values
    assert "User sedang membangun AURA" in values


@patch("core.context_builder.history")
@patch("core.memory_retrieval.search")
@patch("core.context_builder.owner_name")
def test_retrieval_removes_duplicate_memory(
    mock_owner_name,
    mock_search,
    mock_history,
):
    mock_owner_name.return_value = None
    mock_history.return_value = []

    duplicate = {
        "memory_value": "User sedang belajar Python"
    }

    mock_search.return_value = [
        duplicate,
        duplicate,
    ]

    context = build_context(
        "Python Python"
    )

    values = [
        memory["memory_value"]
        for memory in context.memories
    ]

    assert values.count("User sedang belajar Python") == 1


@patch("core.context_builder.history")
@patch("core.memory_retrieval.search")
@patch("core.context_builder.owner_name")
def test_retrieval_handles_no_memory(
    mock_owner_name,
    mock_search,
    mock_history,
):
    mock_owner_name.return_value = None
    mock_search.return_value = []
    mock_history.return_value = []

    context = build_context(
        "topik yang tidak diketahui"
    )

    assert context.memories == []


@patch("core.context_builder.history")
@patch("core.memory_retrieval.search")
@patch("core.context_builder.owner_name")
def test_retrieval_ignores_unmatched_words(
    mock_owner_name,
    mock_search,
    mock_history,
):
    mock_owner_name.return_value = None
    mock_history.return_value = []

    def search_memory(word):
        if word == "python":
            return [
                {
                    "memory_value": "User sedang belajar Python"
                }
            ]

        return []

    mock_search.side_effect = search_memory

    context = build_context(
        "halo aku sedang belajar Python"
    )

    values = [
        memory["memory_value"]
        for memory in context.memories
    ]

    assert values == [
        "User sedang belajar Python"
    ]

def test_score_memory_by_matching_words():
    retrieval = MemoryRetrieval()

    memory = {
        "memory_value": "User sedang belajar Python"
    }

    score = retrieval.score(
        "Aku sedang belajar Python",
        memory,
    )

    assert score > 0

def test_score_relevant_memory_higher():
    retrieval = MemoryRetrieval()

    relevant = {
        "memory_value": "User sedang belajar Python"
    }

    irrelevant = {
        "memory_value": "User suka kopi"
    }

    relevant_score = retrieval.score(
        "Aku sedang belajar Python",
        relevant,
    )

    irrelevant_score = retrieval.score(
        "Aku sedang belajar Python",
        irrelevant,
    )

    assert relevant_score > irrelevant_score

def test_retrieve_ranks_relevant_memory(monkeypatch):
    retrieval = MemoryRetrieval()

    memories = [
        {
            "memory_value": "User suka kopi"
        },
        {
            "memory_value": "User sedang belajar Python"
        },
    ]

    monkeypatch.setattr(
        "core.memory_retrieval.search",
        lambda word: memories,
    )

    result = retrieval.retrieve(
        "Aku sedang belajar Python"
    )

    assert result[0]["memory_value"] == "User sedang belajar Python"

def test_retrieval_normalizes_punctuation(monkeypatch):
    retrieval = MemoryRetrieval()

    monkeypatch.setattr(
        "core.memory_retrieval.search",
        lambda word: (
            [{"memory_value": "User sedang belajar Python"}]
            if word == "python"
            else []
        ),
    )

    result = retrieval.retrieve(
        "Aku sedang belajar Python?"
    )

    assert result == [
        {"memory_value": "User sedang belajar Python"}
    ]

def test_retrieval_limits_memory_results(monkeypatch):
    retrieval = MemoryRetrieval()

    memories = [
        {"memory_value": f"Memory Python {index}"}
        for index in range(10)
    ]

    monkeypatch.setattr(
        "core.memory_retrieval.search",
        lambda word: memories,
    )

    result = retrieval.retrieve(
        "Python"
    )

    assert len(result) <= 5

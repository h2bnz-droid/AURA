from core.context_builder import build_context

def test_build_context_memory(monkeypatch):
    memories = [
        {
            "memory_value": "User belajar Python"
        }
    ]

    monkeypatch.setattr(
        "core.context_builder.owner_name",
        lambda: "Hibban",
    )

    monkeypatch.setattr(
        "core.context_builder.history",
        lambda limit: [],
    )

    monkeypatch.setattr(
        "core.context_builder.memory_retrieval.retrieve",
        lambda user_input: memories,
    )

    context = build_context("belajar Python")

    assert context.memories == memories

def test_build_context_profile(monkeypatch):
    monkeypatch.setattr(
        "core.context_builder.owner_name",
        lambda: "Hibban",
    )

    monkeypatch.setattr(
        "core.context_builder.history",
        lambda limit: [],
    )

    monkeypatch.setattr(
        "core.context_builder.memory_retrieval.retrieve",
        lambda user_input: [],
    )

    context = build_context("halo")

    assert context.profile == "Hibban"

def test_build_context_passes_user_input_to_memory_retrieval(monkeypatch):
    captured = {}

    def fake_retrieve(user_input):
        captured["value"] = user_input
        return []

    monkeypatch.setattr(
        "core.context_builder.owner_name",
        lambda: None,
    )

    monkeypatch.setattr(
        "core.context_builder.history",
        lambda limit: [],
    )

    monkeypatch.setattr(
        "core.context_builder.memory_retrieval.retrieve",
        fake_retrieve,
    )

    build_context("Aku belajar Python")

    assert captured["value"] == "Aku belajar Python"

def test_build_context_requests_six_history_items(monkeypatch):
    captured = {}

    def fake_history(limit):
        captured["limit"] = limit
        return []

    monkeypatch.setattr(
        "core.context_builder.owner_name",
        lambda: None,
    )

    monkeypatch.setattr(
        "core.context_builder.memory_retrieval.retrieve",
        lambda user_input: [],
    )

    monkeypatch.setattr(
        "core.context_builder.history",
        fake_history,
    )

    build_context("Halo")

    assert captured["limit"] == 6

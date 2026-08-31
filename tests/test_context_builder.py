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

def test_build_context_includes_personalization():
    context = build_context("hello")

    assert hasattr(context, "personalization")
    assert isinstance(context.personalization, dict)

def test_context_has_active_mindset():
    context = build_context("halo")

    assert hasattr(context, "active_mindset")
    assert context.active_mindset is None

def test_build_context_includes_mindsets(monkeypatch):
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
        lambda user_input: [],
    )

    context = build_context("halo")

    assert context.mindsets
    assert any(
        mindset.name == "growth"
        for mindset in context.mindsets
    )

def test_build_context_detects_active_mindset(monkeypatch):
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
        lambda user_input: [],
    )
    monkeypatch.setattr(
        "core.context_builder.event_history",
        lambda: [],
    )
    monkeypatch.setattr(
        "core.context_builder.latest_emotion",
        lambda: None,
    )
    monkeypatch.setattr(
        "core.context_builder.latest",
        lambda: [],
    )
    monkeypatch.setattr(
        "core.context_builder.get_all_relationships",
        lambda: [],
    )
    monkeypatch.setattr(
        "core.context_builder.get_all",
        lambda: [],
    )
    monkeypatch.setattr(
        "core.context_builder.collect_long_term_context",
        lambda: [],
    )
    monkeypatch.setattr(
        "core.context_builder.get_mindsets",
        lambda: [],
    )
    monkeypatch.setattr(
        "core.context_builder.detect_mindset",
        lambda user_input: type(
            "Mindset",
            (),
            {
                "name": "growth",
                "description": "Kemampuan dapat berkembang.",
            },
        )(),
    )

    context = build_context("Aku ingin belajar lebih baik.")

    assert context.active_mindset is not None
    assert context.active_mindset.name == "growth"
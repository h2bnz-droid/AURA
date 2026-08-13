from core.context import AuraContext
from core.prompt_builder import PromptBuilder


def test_prompt_builder_includes_user_input():
    context = AuraContext("Halo AURA")

    prompt = PromptBuilder().build(context)

    assert "CURRENT USER MESSAGE" in prompt
    assert "Halo AURA" in prompt


def test_prompt_builder_includes_profile():
    context = AuraContext("Halo")
    context.profile = "Hibban"

    prompt = PromptBuilder().build(context)

    assert "[PROFILE]" in prompt
    assert "Nama: Hibban" in prompt


def test_prompt_builder_includes_memory():
    context = AuraContext("Apa yang sedang kupelajari?")

    context.memories = [
        {"memory_value": "User sedang belajar Python"},
        {"memory_value": "User sedang membangun AURA"},
    ]

    prompt = PromptBuilder().build(context)

    assert "[MEMORY]" in prompt
    assert "- User sedang belajar Python" in prompt
    assert "- User sedang membangun AURA" in prompt


def test_prompt_builder_includes_history():
    context = AuraContext("Lanjutkan")

    context.history = [
        {"role": "User", "message": "Aku sedang belajar Python"},
        {"role": "AURA", "message": "Bagus, lanjutkan latihanmu."},
    ]

    prompt = PromptBuilder().build(context)

    assert "[RECENT CONVERSATION]" in prompt
    assert "User: Aku sedang belajar Python" in prompt
    assert "AURA: Bagus, lanjutkan latihanmu." in prompt

def test_prompt_builder_handles_empty_context():
    context = AuraContext("Halo")

    prompt = PromptBuilder().build(context)

    assert "Halo" in prompt
    assert "[PROFILE]" not in prompt
    assert "[MEMORY]" not in prompt
    assert "[RECENT CONVERSATION]" not in prompt

def test_prompt_builder_preserves_section_order():
    context = AuraContext("Apa kabar?")

    context.profile = "Hibban"
    context.memories = [
        {"memory_value": "User sedang belajar Python"},
    ]
    context.history = [
        {"role": "User", "message": "Halo"},
    ]

    prompt = PromptBuilder().build(context)

    profile_index = prompt.index("[PROFILE]")
    memory_index = prompt.index("[MEMORY]")
    history_index = prompt.index("[RECENT CONVERSATION]")
    current_index = prompt.index("CURRENT USER MESSAGE")

    assert profile_index < memory_index
    assert memory_index < history_index
    assert history_index < current_index

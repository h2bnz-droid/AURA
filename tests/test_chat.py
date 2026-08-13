from unittest.mock import patch

from core.chat import ask
from core.context import AuraContext


@patch("core.chat.chat")
@patch("core.chat.add")
@patch("core.chat.build_context")
def test_ask_saves_user_and_aura_messages(
    mock_build_context,
    mock_add,
    mock_chat,
):
    mock_context = AuraContext("Halo AURA")
    mock_build_context.return_value = mock_context

    mock_chat.return_value = "Halo juga!"

    result = ask("Halo AURA")

    assert result == "Halo juga!"

    assert mock_add.call_count == 2

    mock_add.assert_any_call(
        "User",
        "Halo AURA",
    )

    mock_add.assert_any_call(
        "AURA",
        "Halo juga!",
    )

@patch("core.chat.chat")
@patch("core.chat.add")
@patch("core.chat.build_context")
def test_ask_handles_empty_context(
    mock_build_context,
    mock_add,
    mock_chat,
):
    mock_build_context.return_value = AuraContext(
        "Halo"
    )

    mock_chat.return_value = "Halo!"

    result = ask("Halo")

    assert result == "Halo!"
    mock_chat.assert_called_once()

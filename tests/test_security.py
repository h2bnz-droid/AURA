import pytest

from core.security import (
    MAX_INPUT_LENGTH,
    InputValidationError,
    redact_sensitive_data,
    validate_user_input,
)


def test_valid_input_is_trimmed():
    result = validate_user_input("  halo AURA  ")

    assert result == "halo AURA"


def test_empty_input_is_rejected():
    with pytest.raises(InputValidationError):
        validate_user_input("")


def test_whitespace_input_is_rejected():
    with pytest.raises(InputValidationError):
        validate_user_input("   ")


def test_non_string_input_is_rejected():
    with pytest.raises(InputValidationError):
        validate_user_input(123)


def test_oversized_input_is_rejected():
    oversized_input = "a" * (MAX_INPUT_LENGTH + 1)

    with pytest.raises(InputValidationError):
        validate_user_input(oversized_input)


def test_maximum_length_input_is_allowed():
    valid_input = "a" * MAX_INPUT_LENGTH

    result = validate_user_input(valid_input)

    assert result == valid_input

def test_api_key_is_redacted():
    result = redact_sensitive_data(
        "api_key=abc123"
    )

    assert result == "api_key=[REDACTED]"


def test_bearer_token_is_redacted():
    result = redact_sensitive_data(
        "Bearer abc123token"
    )

    assert result == "Bearer [REDACTED]"


def test_password_is_redacted():
    result = redact_sensitive_data(
        "password=my-secret"
    )

    assert result == "password=[REDACTED]"


def test_secret_is_redacted():
    result = redact_sensitive_data(
        "secret: hidden-value"
    )

    assert result == "secret: [REDACTED]"


def test_token_is_redacted():
    result = redact_sensitive_data(
        "token=abc-token"
    )

    assert result == "token=[REDACTED]"


def test_normal_text_is_preserved():
    result = redact_sensitive_data(
        "Saya sedang belajar Python."
    )

    assert result == "Saya sedang belajar Python."
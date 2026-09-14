from __future__ import annotations

import re


MAX_INPUT_LENGTH = 4000

REDACTED_VALUE = "[REDACTED]"


class InputValidationError(ValueError):
    """Raised when user input is invalid."""


def validate_user_input(user_message: str) -> str:
    """
    Validate and normalize user input before entering the AURA pipeline.
    """

    if not isinstance(user_message, str):
        raise InputValidationError(
            "User input must be a string."
        )

    normalized_message = user_message.strip()

    if not normalized_message:
        raise InputValidationError(
            "User input cannot be empty."
        )

    if len(normalized_message) > MAX_INPUT_LENGTH:
        raise InputValidationError(
            "User input exceeds the maximum allowed length."
        )

    return normalized_message


def redact_sensitive_data(value: str) -> str:
    """
    Redact common secret-like values before they enter AI context.
    """

    if not isinstance(value, str):
        return value

    patterns = [
        (
            r"(?i)(bearer\s+)[A-Za-z0-9._\-]+",
            rf"\1{REDACTED_VALUE}",
        ),
        (
            r"(?i)(api[_-]?key\s*[:=]\s*)\S+",
            rf"\1{REDACTED_VALUE}",
        ),
        (
            r"(?i)(password\s*[:=]\s*)\S+",
            rf"\1{REDACTED_VALUE}",
        ),
        (
            r"(?i)(secret\s*[:=]\s*)\S+",
            rf"\1{REDACTED_VALUE}",
        ),
        (
            r"(?i)(token\s*[:=]\s*)\S+",
            rf"\1{REDACTED_VALUE}",
        ),
    ]

    sanitized_value = value

    for pattern, replacement in patterns:
        sanitized_value = re.sub(
            pattern,
            replacement,
            sanitized_value,
        )

    return sanitized_value
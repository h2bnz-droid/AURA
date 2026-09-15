from core.fallback import (
    DEFAULT_FALLBACK_RESPONSE,
    get_fallback_response,
)


def test_fallback_response_is_non_empty():
    assert get_fallback_response().strip()


def test_fallback_response_is_stable():
    assert get_fallback_response() == DEFAULT_FALLBACK_RESPONSE


def test_fallback_response_does_not_expose_internal_details():
    response = get_fallback_response()

    assert "traceback" not in response.lower()
    assert "ollama" not in response.lower()
    assert "exception" not in response.lower()

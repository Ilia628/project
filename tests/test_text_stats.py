import pytest

from src.text_stats import (
    average_word_length,
    count_sentences,
    count_words,
    analyze_text,
)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привет, мир!", 2),
        ("GitHub Actions запускает скрипт.", 4),
        ("", 0),
        ("Строка с 123 числами.", 4),
    ],
)
def test_count_words(text: str, expected: int) -> None:
    assert count_words(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привет, мир!", 1),
        ("Один. Два? Три!", 3),
        ("", 0),
    ],
)
def test_count_sentences(text: str, expected: int) -> None:
    assert count_sentences(text) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Привет, мир!", 4.5),
        ("", 0.0),
    ],
)
def test_average_word_length(text: str, expected: float) -> None:
    assert average_word_length(text) == expected


def test_analyze_text_returns_expected_values() -> None:
    result = analyze_text("Тест. Работает!")
    assert result == {
        "words": 2,
        "sentences": 2,
        "average_word_length": 6.0,
    }

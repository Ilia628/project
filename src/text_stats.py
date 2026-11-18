import re
from typing import Dict


WORD_RE = re.compile(r"\b\w+\b", flags=re.UNICODE)
SENTENCE_RE = re.compile(r"[.!?]+")


def count_words(text: str) -> int:
    """Подсчитывает количество слов в тексте."""
    return len(WORD_RE.findall(text))


def count_sentences(text: str) -> int:
    """Подсчитывает количество предложений в тексте."""
    return len(SENTENCE_RE.findall(text))


def average_word_length(text: str) -> float:
    """Вычисляет среднюю длину слова."""
    words = WORD_RE.findall(text)
    if not words:
        return 0.0
    return round(sum(len(word) for word in words) / len(words), 2)


def analyze_text(text: str) -> Dict[str, object]:
    """Возвращает словарь с результатами анализа текста."""
    return {
        "words": count_words(text),
        "sentences": count_sentences(text),
        "average_word_length": average_word_length(text),
    }

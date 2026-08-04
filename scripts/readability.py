#!/usr/bin/env python3
"""Estimate Flesch Reading Ease for English prose.

The tokenizer is deterministic and dependency-free. It approximates Flesch's
manual counting method, so its result may differ from other implementations.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


FENCED_CODE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:https?://|www\.)[^)]+\)", re.IGNORECASE)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
URL_RE = re.compile(r"\b(?:https?://|www\.)\S+", re.IGNORECASE)
NUMERIC_TOKEN_RE = re.compile(
    r"(?<![\w])(?:[$€£¥])?[+-]?\d[\d,]*(?:[.:/-]\d+)*(?:%)?(?![\w])"
)
WORD_RE = re.compile(r"[^\W\d_]+(?:['-][^\W\d_]+)*", re.UNICODE)
SENTENCE_SPLIT_RE = re.compile(r"[.!?]+[\"'”’\)\]]*")
VOWEL_GROUP_RE = re.compile(r"[aeiouy]+")

SYLLABLE_EXCEPTIONS = {
    "business": 2,
    "comfortable": 3,
    "different": 3,
    "every": 2,
    "family": 3,
    "interesting": 4,
    "little": 2,
    "people": 2,
    "queue": 1,
}


def clean_text(text: str) -> str:
    """Remove content that should not affect the prose score."""
    cleaned = FENCED_CODE_RE.sub(" ", text)
    cleaned = MARKDOWN_LINK_RE.sub(r"\1", cleaned)
    cleaned = INLINE_CODE_RE.sub(" ", cleaned)
    cleaned = URL_RE.sub(" ", cleaned)
    cleaned = cleaned.replace("’", "'").replace("‘", "'")
    cleaned = cleaned.replace("‐", "-").replace("‑", "-")
    cleaned = cleaned.replace("–", " ").replace("—", " ")
    return NUMERIC_TOKEN_RE.sub(" ", cleaned)


def extract_words(text: str) -> list[str]:
    """Return alphabetic words, keeping contractions and hyphenated terms whole."""
    return WORD_RE.findall(text)


def count_sentences(text: str) -> int:
    """Count punctuated thought-like segments that contain scorable words."""
    segments = SENTENCE_SPLIT_RE.split(text)
    count = sum(1 for segment in segments if extract_words(segment))
    return max(count, 1) if extract_words(text) else 0


def _count_word_part(part: str) -> int:
    normalized = re.sub(r"[^a-z]", "", part.lower())
    if not normalized:
        return 0
    if normalized in SYLLABLE_EXCEPTIONS:
        return SYLLABLE_EXCEPTIONS[normalized]
    if len(normalized) <= 3:
        return 1

    count = len(VOWEL_GROUP_RE.findall(normalized))

    if normalized.endswith("e") and not normalized.endswith("le") and count > 1:
        count -= 1
    if normalized.endswith("ed") and len(normalized) > 3:
        preceding = normalized[-3]
        if preceding not in "td" and count > 1:
            count -= 1
    if normalized.endswith("es") and len(normalized) > 3:
        if not normalized.endswith(("ses", "xes", "zes", "ches", "shes")) and count > 1:
            count -= 1

    return max(count, 1)


def count_syllables(word: str) -> int:
    """Estimate English syllables in one scorable word."""
    without_apostrophes = word.replace("'", "")
    return max(sum(_count_word_part(part) for part in without_apostrophes.split("-")), 1)


def flesch_reading_ease(words: int, sentences: int, syllables: int) -> float:
    """Calculate the published Flesch Reading Ease formula."""
    if words <= 0 or sentences <= 0:
        raise ValueError("Flesch Reading Ease requires scorable words and sentences.")
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)


def analyse(text: str) -> dict[str, Any]:
    """Return deterministic readability statistics for text."""
    cleaned = clean_text(text)
    words = extract_words(cleaned)
    if not words:
        raise ValueError("No scorable English words found.")

    sentence_count = count_sentences(cleaned)
    syllable_count = sum(count_syllables(word) for word in words)
    word_count = len(words)
    average_sentence_length = word_count / sentence_count
    score = flesch_reading_ease(word_count, sentence_count, syllable_count)

    return {
        "scorable_words": word_count,
        "sentences": sentence_count,
        "estimated_syllables": syllable_count,
        "average_sentence_length": round(average_sentence_length, 1),
        "flesch_reading_ease": round(score, 1),
        "confidence": "standard" if word_count >= 100 else "short-sample",
    }


def read_input(path: str | None) -> str:
    if path in (None, "-"):
        return sys.stdin.read()
    try:
        return Path(path).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        raise ValueError(f"Could not read {path}: {error}") from error


def format_human(result: dict[str, Any]) -> str:
    confidence = result["confidence"]
    confidence_note = "100+ words counted" if confidence == "standard" else "fewer than 100 words counted"
    score = result["flesch_reading_ease"]
    if score >= 90:
        score_context = "very easy"
    elif score >= 80:
        score_context = "easy"
    elif score >= 70:
        score_context = "fairly easy"
    elif score >= 60:
        score_context = "standard"
    elif score >= 50:
        score_context = "fairly difficult"
    elif score >= 30:
        score_context = "difficult"
    else:
        score_context = "very difficult"

    sentence_length = result["average_sentence_length"]
    if sentence_length < 15:
        sentence_context = "short"
    elif sentence_length <= 20:
        sentence_context = "moderate"
    elif sentence_length <= 25:
        sentence_context = "long"
    else:
        sentence_context = "very long"

    return "\n".join(
        [
            f"Flesch Reading Ease (estimated; roughly {score_context}): {score}",
            f"Words counted: {result['scorable_words']}",
            f"Sentences: {result['sentences']}",
            f"Estimated syllables: {result['estimated_syllables']}",
            f"Average sentence length (rough context: {sentence_context}): {result['average_sentence_length']} words",
            f"Confidence: {confidence} ({confidence_note})",
        ]
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Estimate Flesch Reading Ease for English prose. Reads stdin when no file is given."
    )
    parser.add_argument("path", nargs="?", help="UTF-8 text file, or - for stdin")
    parser.add_argument("--json", action="store_true", help="Emit a JSON object")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        result = analyse(read_input(args.path))
    except ValueError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    else:
        print(format_human(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

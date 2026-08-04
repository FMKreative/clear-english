#!/usr/bin/env python3

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from readability import analyse, clean_text, extract_words, flesch_reading_ease


SCRIPT = Path(__file__).with_name("readability.py")


class ReadabilityTests(unittest.TestCase):
    def test_published_formula_from_known_counts(self) -> None:
        score = flesch_reading_ease(words=100, sentences=5, syllables=150)
        self.assertAlmostEqual(score, 59.635, places=3)

    def test_analysis_matches_independent_formula(self) -> None:
        result = analyse("Clear prose helps people. Simple words can carry exact meaning.")
        expected = 206.835 - 1.015 * (
            result["scorable_words"] / result["sentences"]
        ) - 84.6 * (result["estimated_syllables"] / result["scorable_words"])
        self.assertEqual(result["flesch_reading_ease"], round(expected, 1))

    def test_contractions_and_hyphenated_terms_are_single_words(self) -> None:
        words = extract_words(clean_text("We're testing a well-known method."))
        self.assertEqual(words, ["We're", "testing", "a", "well-known", "method"])

    def test_unicode_apostrophe_and_punctuation(self) -> None:
        result = analyse("“We’re ready!” She agreed. Is it clear?")
        self.assertEqual(result["sentences"], 3)
        self.assertIn("We're", extract_words(clean_text("We’re ready.")))

    def test_markdown_code_and_urls_are_excluded(self) -> None:
        text = """Keep this [plain link](https://example.com). Ignore `secret code`.

```python
hidden words should not count
```
"""
        words = extract_words(clean_text(text))
        self.assertEqual(words, ["Keep", "this", "plain", "link", "Ignore"])

    def test_numeric_and_symbolic_tokens_are_excluded(self) -> None:
        words = extract_words(clean_text("There were 2026 items worth $50 and 4.5%."))
        self.assertEqual(words, ["There", "were", "items", "worth", "and"])

    def test_numeric_exclusion_preserves_sentence_endings(self) -> None:
        result = analyse("It happened in 2026. We recorded 4.5%.")
        self.assertEqual(result["sentences"], 2)

    def test_empty_and_unscorable_input_fail(self) -> None:
        for text in ("", "   ", "1234 $50 4.5%"):
            with self.subTest(text=text):
                with self.assertRaisesRegex(ValueError, "No scorable English words"):
                    analyse(text)

    def test_confidence_boundary(self) -> None:
        short = analyse(" ".join(["word"] * 99) + ".")
        standard = analyse(" ".join(["word"] * 100) + ".")
        self.assertEqual(short["confidence"], "short-sample")
        self.assertEqual(standard["confidence"], "standard")

    def test_cli_json_from_stdin(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT), "--json"],
            input="Clear text is useful.",
            text=True,
            capture_output=True,
            check=True,
        )
        result = json.loads(completed.stdout)
        self.assertEqual(result["scorable_words"], 4)
        self.assertEqual(result["confidence"], "short-sample")

    def test_cli_reads_utf8_file(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.txt"
            path.write_text("We’re writing clear English.", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPT), str(path), "--json"],
                text=True,
                capture_output=True,
                check=True,
            )
        result = json.loads(completed.stdout)
        self.assertEqual(result["scorable_words"], 4)

    def test_cli_returns_error_for_unscorable_input(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT)],
            input="1234 $50",
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(completed.returncode, 2)
        self.assertIn("No scorable English words", completed.stderr)


if __name__ == "__main__":
    unittest.main()

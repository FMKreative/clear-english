# Clear English

Clear English is a Codex skill for rewriting, summarizing, explaining, and simplifying supplied English. It makes writing clearer and more natural for broad adult audiences, including non-native English speakers, without changing the meaning or voice.

## Use it when you want to

- rewrite unclear, formal, or overly dense writing
- simplify technical or academic language
- summarize a passage faithfully
- explain a difficult passage using the supplied source

## Use it

Invoke the skill with a request such as:

```text
Use $clear-english to rewrite this text in clear, natural English while preserving its meaning and tone.
```

You can also specify the format, audience, length, or readability target you need.

## What it preserves

The skill keeps facts, numbers, names, attribution, uncertainty, conditions, warnings, necessary detail, and tone. It uses the supplied source and does not add unsupported information.

It measures substantial rewrites with Flesch Reading Ease and average sentence length. These metrics describe surface difficulty; they are not proof of quality, comprehension, or usefulness.

## Repository guide

| File | Purpose |
| --- | --- |
| [`SKILL.md`](SKILL.md) | Operating instructions and writing rules |
| [`scripts/readability.py`](scripts/readability.py) | Readability measurement utility |
| [`scripts/test_readability.py`](scripts/test_readability.py) | Readability tests |
| [`evals/`](evals/) | Representative evaluation cases |
| [`references/principles.md`](references/principles.md) | Rationale, sources, limitations, and release guidance |
| [`VERSION`](VERSION) | Current release version |

## Development

Run the tests with:

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
```

Measure a text file with:

```bash
python3 scripts/readability.py path/to/file.txt
```

See [`LICENSE`](LICENSE) for licensing information.

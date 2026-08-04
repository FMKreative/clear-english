---
name: clear-english
description: Rewrite, summarize, explain, and simplify existing English source text so it is clear, direct, natural, and easier for broad or non-native adult audiences to understand while preserving meaning, facts, uncertainty, necessary detail, and tone. Use when a user asks to clarify their writing, remove fluff or AI-like language, produce a faithful plain-English summary, explain a difficult supplied passage, or simplify source material without adding outside knowledge.
---

# Clear English

Transform supplied English without weakening its meaning or replacing its voice. Treat clarity as a reader outcome, not a demand for uniformly short prose.

## Workflow

1. **Identify the operation.** Infer whether the user wants a rewrite, summary, explanation, or simplification. Follow any requested length, format, dialect, or audience. Otherwise write for a broad adult audience that includes non-native English speakers.
2. **Set the source boundary.** Use only information the user supplies as source material. Do not add outside knowledge, invented examples, unsupported claims, or explanations that the source does not support. If the source lacks information needed to explain something, state the gap.
3. **Record the invariants.** Preserve names, facts, dates, numbers, attribution, uncertainty, conditions, warnings, necessary terminology, intended meaning, and tone. In a summary, preserve every qualification needed to keep each retained claim accurate.
4. **Transform the text.** Apply the editing principles below. A summary may omit detail, but must not distort a claim by removing its context or caveat. An explanation may make supported relationships explicit, but must not import new facts.
5. **Check fidelity.** Compare the result with the source. Restore any lost qualification, scope, responsibility, sequence, or emotional character. Do not make a tentative claim certain or an opinion factual.
6. **Measure after editing.** For substantial text, run the readability script after the language work is complete. Report the result with a brief, plain-language interpretation; never revise merely to improve the score.
7. **Return the result first.** Do not describe the edits unless the user asks.

## Editing principles

- Lead with the main point.
- Use familiar, precise words when they carry the same meaning.
- Prefer concrete nouns and strong verbs.
- Remove repetition, empty transitions, inflated wording, and needless modifiers.
- Keep most sentences focused on one main idea, but vary their length to preserve rhythm.
- Prefer active voice when the actor matters. Keep passive voice when it is more accurate or natural.
- Use short paragraphs and informative headings when they make longer text easier to navigate.
- Keep necessary technical terms. Explain them only when the supplied source provides enough information.
- State what something is when that is clearer than stating what it is not. Do not force an optimistic tone.
- Break any mechanical rule when accuracy, meaning, tone, or natural English requires it.

Avoid childish language, literary imitation, generic introductions, repeated conclusions, excessive headings, canned transitions, stacked adjectives, needless hedging, and strings of uniformly short sentences.

## Tone

Preserve the source's personality, formality, stance, and emotional character in every operation. Simplify within that voice. Do not replace an informal voice with corporate prose or flatten formal, promotional, humorous, urgent, or personal language into a neutral house style.

If tone and simplification conflict, preserve the tone and improve only what can change without damaging it.

## Readability

Treat 100 words counted by the script as the threshold for a standard sample. Run `python3 scripts/readability.py <path>` from this skill directory, or send text through stdin. Use `--json` when structured output is useful.

- Add a readability note only for substantial text. Omit it for shorter text unless the user asks for it.
- For a rewrite with substantial original and revised text, report both results.
- For a substantial summary, explanation, or simplification without a comparable original, report the final result.
- Call Flesch Reading Ease an estimate of surface difficulty, not a quality score. Never use it as proof of clarity, accuracy, coherence, or usefulness.
- Give the score a rough reference: 90–100 is very easy, 80–89 easy, 70–79 fairly easy, 60–69 standard, 50–59 fairly difficult, 30–49 difficult, and 0–29 very difficult. These ranges are orientation, not targets, and can misrepresent technical or specialized writing.
- Explain average sentence length with rough context: under 15 words is short, 15–20 moderate, 21–25 long, and over 25 very long. These are not universal rules or goals; genre and sentence structure matter.
- Do not include “Scorable words” in the default reader-facing note. It means the number of ordinary English words included in the calculation after the script removes code, links, URLs, numbers, and symbols. If the count is useful for explaining a short sample or comparing two versions, call it “Words counted” and explain it briefly. It is not a quality measure.

Append a compact block after the transformed text. Include the parenthetical context so the numbers do not stand alone:

```text
Readability
- Flesch Reading Ease: 58.4 -> 71.2 (estimated; from fairly difficult to standard)
- Average sentence length: 20.9 -> 15.1 words (both around moderate; rough context only)
```

For one result, show one value instead of a comparison.

## Maintenance reference

Read [references/principles.md](references/principles.md) only when reviewing the rationale, maintaining the rules, or planning a later version. Do not load it for routine transformations.

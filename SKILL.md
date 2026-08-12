---
name: clear-english
description: Rewrite, summarize, explain, and simplify existing English source text so it is clear, direct, natural, and easier for broad or non-native adult audiences to understand while preserving meaning, facts, uncertainty, necessary detail, and tone. Use when a user asks to clarify their writing, remove fluff or AI-like language, produce a faithful plain-English summary, explain a difficult supplied passage, or simplify source material without adding outside knowledge.
---

# Clear English

Transform supplied English without weakening its meaning or replacing its voice. Treat clarity as a reader outcome, not a demand for uniformly short prose.

## Priorities

Resolve conflicts in this order: (1) accuracy and source fidelity, (2) required meaning, qualifications, tone, and user-required terms, (3) requested format and length, then (4) readability target.

## Workflow

1. **Identify the operation.** Infer whether the user wants a rewrite, summary, explanation, or simplification. Follow requested constraints. Otherwise write for a broad adult audience that includes non-native English speakers.
2. **Set the target silently.** For substantial text, require at least 60, prefer 60–89, and aim near 80 to leave room for the formula's estimate. Accept scores above 89. Replace the default with any explicit target: treat “score 70” or “around 70” as 65–75, “at least 70” as 70 or higher, and a stated range as bounded at both ends. Never ask the user to choose or confirm a score.
3. **Set boundaries.** Use only supplied source material. Preserve names, facts, numbers, attribution, uncertainty, conditions, warnings, meaning, and tone. Fidelity protects meaning, not wording or academic register. Do not add outside knowledge or unsupported claims. Mention a source gap only when silence would mislead.
4. **Plan plain wording.** Before drafting, replace each long or abstract phrase that has a shorter accurate equivalent. Keep a specialized term only when the user requires it or replacement would lose meaning. A term is not required merely because the source uses it.
5. **Draft once.** Apply the principles below in one language pass. Summaries may omit detail but must keep the context and caveats needed for each claim. Explanations may make supported relationships explicit but may not import facts.
6. **Check fidelity before scoring.** Restore lost scope, responsibility, sequence, qualifications, or emotional character within the same pass. Keep tentative claims tentative and opinions identifiable as opinions.
7. **Measure once.** Score only the final text after the fidelity check. Score the original only when the user requests a comparison. Never generate or revise another version after seeing the score.
8. **Return the result first.** On a miss, return the best faithful version, actual score, and one brief note. Do not retry, ask what to do, or describe edits unless requested.

## Editing principles

- Lead with the main point. Use familiar, precise words and direct verbs.
- Translate supported labels into plain meaning: “a study over time” for “a longitudinal study” or “make the new value appear at once” for “provide immediate consistency.” Keep exact terms such as “statistically significant” when the claim requires them.
- Break dense noun phrases into clauses with clear actors. Separate claims, conditions, causes, and qualifications.
- In dense prose, aim for 8–12 words in sentences containing necessary long terms. Name a term once, then use an unambiguous short reference.
- Remove repetition, inflated wording, needless modifiers, and empty transitions. Do not pad the text or create strings of fragments.
- Prefer active voice when the actor matters. Use short paragraphs or headings when they help.
- Break any mechanical rule when accuracy, tone, or natural English requires it. Avoid childish language and do not force an optimistic tone.

## Tone

Preserve personality, formality, stance, and emotional character. Simplify within that voice; if tone and simplification conflict, preserve tone.

## Readability

Treat 100 counted words as substantial text and a standard sample. Run `python3 scripts/readability.py <path>` from this directory or send the final text through stdin. Use `--json` for structured output.

- Target and report readability by default only for substantial text. Measure shorter text only when asked and call it a short-sample estimate.
- Report only the final result unless the user asks for an original-to-final comparison.
- Treat Flesch Reading Ease as an estimate of surface difficulty, not proof of clarity, accuracy, coherence, comprehension, or usefulness.
- Give the score a rough reference: 90–100 is very easy, 80–89 easy, 70–79 fairly easy, 60–69 standard, 50–59 fairly difficult, 30–49 difficult, and 0–29 very difficult. These labels describe surface difficulty and can misrepresent technical or specialized writing.
- Report average words per sentence to one decimal place with the label short, moderate, long, or very long. Treat it as orientation, not a goal.
- Omit “Scorable words” from the default note. If the count helps explain a short sample or comparison, call it “Words counted.”

Append a compact block after the transformed text. Include the parenthetical context so the numbers do not stand alone:

```text
Readability
- Flesch Reading Ease: 71.2 (fairly easy)
- Average sentence length: 15.1 words (moderate)
```

## Maintenance reference

Read [references/principles.md](references/principles.md) only when reviewing the rationale, maintaining the rules, or planning a later version. Do not load it for routine transformations.

# Reader-Effort Clarity for Existing English

## Problem Statement

How might we make existing user-authored or user-provided English as easy to read as possible, while preserving meaning, facts, uncertainty, necessary detail, stance, and tone?

## Recommended Direction

Add a lightweight reader-effort quality gate to the existing one-pass workflow, supported by evaluation cases that cover both user-authored drafts and text provided from other sources.

The gate should make readability the strongest optimization after factual meaning and necessary safeguards. It should check whether the final text makes the main point, actors, relationships, sequence, conditions, and qualifications easier to follow. It should protect the writer’s stance and emotional character without preserving stiff wording or unnecessary formality.

The evaluation layer should test this across broad domains: academic, technical, policy, general, and product/UI copy. It should include drafts written by the user as well as formal source-like text. Flesch Reading Ease remains a surface estimate, not the definition of success.

The initial quantitative target is a minimum average Flesch Reading Ease of 65 across the fixed rewritten-output benchmark. This is an aggregate target, not a minimum for every case. Fidelity and naturalness remain required even when a case scores below 65.

Report the overall average alongside averages by domain and input type. Use the qualitative guardrails in `evals/quality-rubric.md` to reject score improvements that weaken meaning, necessary terminology, warnings, uncertainty, stance, or tone.

The first revised one-pass snapshot averaged 71.9, compared with 49.4 for the original snapshot. After restoring source distinctions identified during the fidelity review, the fidelity-checked snapshot averages 68.2. It clears the 65 overall target, with provided-source text at 66.6 and user-authored text at 72.3. Domain averages remain diagnostic rather than separate pass criteria because necessary academic and technical terms can lower Flesch scores.

## Key Assumptions to Validate

- [ ] The main weakness in current outputs is unnecessary reading effort, not missing factual safeguards or loss of intent. Test user-authored drafts and provided source text separately.
- [ ] Readability can be improved substantially without flattening the writer’s stance or emotional character. Test persuasive, branded, and personal examples as well as neutral prose.
- [ ] A short reader-effort gate improves drafting decisions without making the workflow mechanical. Compare a small set with and without the revised guidance.
- [ ] Reader-effort judgments can be made without requiring a second rewrite loop. Keep the check inside the existing fidelity pass.
- [ ] The fixed rewritten-output benchmark averages at least 65 without weakening fidelity. Measure the average after each guidance change and inspect low-scoring cases individually.

## MVP Scope

- Refine `SKILL.md` so maximum readability is the strongest optimization after meaning, necessary detail, and safeguards.
- Define the gate in practical terms: main point, actors, relationships, sequence, conditions, qualifications, natural phrasing, and unnecessary formality.
- Clarify that the skill improves existing user-authored or user-provided text; it does not require the text to come from an external source.
- Add a small set of evaluation cases covering accurate-but-stiff language across existing domains, with both user-authored drafts and provided source text.
- Add evaluation criteria for:
  - preserved meaning and scope
  - preserved warnings, conditions, and uncertainty
  - maximum practical readability
  - preserved stance and emotional character
  - easier-to-follow structure
  - no unsupported additions
- Record a fixed baseline-output snapshot and report its average Flesch Reading Ease. Use `>=65` as the first acceptance threshold.
- Report benchmark results by domain and input type so high-scoring short copy cannot hide weak technical or academic results.
- Review each output with the fidelity and naturalness guardrails in `evals/quality-rubric.md`.
- Keep the existing one-pass drafting and single final measurement workflow.

## Not Doing

- Building a UI-only mode or automatic UI-surface detector — it would narrow a broadly useful skill.
- Replacing human judgment with a new readability score — formulas cannot define naturalness or comprehension.
- Adding a second rewrite loop after measurement — it would conflict with the current bounded workflow.
- Bundling ASD-STE100 or another controlled-language standard — the project explicitly values natural language and tone.
- Generating copy from a brief with no existing draft — that is a separate writing and ideation task.
- Rewriting every text into the same voice or sentence length — maximum readability is not uniform shortness or a generic voice.

## Open Questions

- Which reader-effort checks produce the clearest improvement without becoming a mechanical checklist?
- How much can readability improve before a writer reasonably says the result no longer sounds like them?
- How should the skill handle text that is natural for its intended specialist audience but difficult for a broad reader?
- What counts as evidence that a rewrite is “easier to read” when no reader study is available?

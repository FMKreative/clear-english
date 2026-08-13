# Baseline Quality Rubric

Flesch Reading Ease is the quantitative part of the benchmark. It is not a substitute for checking whether the rewrite remains faithful and useful.

Review each rewritten output against these guardrails:

- [ ] Meaning and scope are unchanged.
- [ ] Names, facts, numbers, required terms, and attribution are preserved.
- [ ] Conditions, warnings, limitations, uncertainty, and sequence are preserved.
- [ ] The writer’s stance and emotional character remain recognizable.
- [ ] The rewrite adds no unsupported facts, explanations, or promises.
- [ ] The main point, actors, relationships, and next meaning are easier to follow.
- [ ] Wording is natural and direct without becoming childish, generic, or fragmented.

## Benchmark rule

The fixed benchmark passes its quantitative target when the average final-output Flesch Reading Ease is at least 65. This is an aggregate target. A low-scoring technical or academic case may remain acceptable when its terminology is necessary and all quality guardrails pass.

Do not change the benchmark cases or omit low-scoring cases to reach the average. Do not rewrite an output again only because its score is low. Record the score, inspect the fidelity guardrails, and improve the drafting guidance for the next benchmark run.

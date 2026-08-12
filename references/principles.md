# Principles and provenance

Use this reference when maintaining the skill or planning a later version. The operating rules belong in `SKILL.md`; do not load this file for routine transformations.

## Versioning and releases

Keep the skill name and folder stable as `clear-english`. Record the installed release in the root `VERSION` file and publish the same number as a Git tag and GitHub Release, prefixed with `v` (for example, `VERSION` contains `1.0.0` and the release tag is `v1.0.0`).

Use semantic versioning for future changes:

- Patch (`1.0.1`) for fixes that preserve the skill's intended behavior.
- Minor (`1.1.0`) for backward-compatible capabilities or meaningful rule improvements.
- Major (`2.0.0`) for changed defaults, boundaries, or output contracts that may surprise existing users.

For each release, update `VERSION`, validate and test the skill, commit the change, create the matching tag, and summarize user-visible changes in the GitHub Release notes. GitHub Releases are the changelog; do not add a separate changelog file. Users can compare their local `VERSION` with the latest GitHub Release. A Git clone can also use `git describe --tags --always` and update with Git; a release archive should be replaced with a newer tagged archive.

## Writing sources

### George Orwell

Primary source: [Politics and the English Language](https://www.orwellfoundation.com/the-orwell-foundation/orwell/essays-and-other-%20works/politics-and-the-english-language/)

Use Orwell's essay to support exact wording, familiar words, removal of needless text, concrete language, active voice when useful, and resistance to stale phrases or jargon. Retain his escape clause in substance: clarity and humane language matter more than mechanical obedience to a rule.

### The Kansas City Star

Primary facsimile: [The Star Copy Style](https://jollycontrarian.com/images/2/26/Kansas_Star_style_guide.pdf)

The facsimile says two early versions survive and neither has a confirmed date. It identifies the reproduced sheet as probably used around 1915 and says Hemingway likely received this or a similar version while working at the newspaper in 1917 and 1918. Treat the rules as the Star's newsroom guidance, not rules authored by Hemingway.

Adapt its durable principles: focused sentences, direct openings, vigorous and exact wording, removal of superfluous text, restraint with adjectives, fresh rather than stale phrasing, and natural rhythm. Do not carry forward period-specific house style, obsolete usage, offensive language, or rigid grammar rules.

### Digital.gov

Modern guidance: [Plain language guide series](https://digital.gov/guides/plain-language/)

Use its reader-centered practices: write for the actual audience, organize around what readers need, put the purpose and important information early, prefer familiar terms, uncover hidden verbs, and use active voice when it clarifies responsibility. Plain language must not mean writing for children unless children are the audience.

### ASD-STE100 Simplified Technical English

Primary source: [ASD-STE100 Simplified Technical English](https://www.asd-ste100.org/), Issue 9, 15 January 2025, rule 9.1.

Adapt its instruction to recast a sentence when word-for-word replacement is insufficient or changes the meaning. Do not adopt or bundle the standard, its controlled vocabulary, hard sentence limits, or other compliance rules. Clear English applies to broader forms of writing and must preserve natural language, meaning, and tone.

## Readability sources

### Rudolf Flesch

Primary paper: [A New Readability Yardstick](https://comp311.wordpress.com/wp-content/uploads/2010/11/flesch_rudolph.pdf)

Use the 1948 paper as the authority for Reading Ease:

`206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word`

Flesch used sentence length and syllables as measurable proxies for difficulty. The paper also describes shortcomings, manual counting conventions, and sampling around 100 words. The bundled script automates these ideas with documented, deterministic approximations; it does not claim to reproduce a human count exactly.

### William H. DuBay

Research survey: [The Principles of Readability](https://files.eric.ed.gov/fulltext/ED490073.pdf)

Use the survey as support for cautious interpretation. Merely shortening words and sentences does not reliably improve comprehension. Content, organization, coherence, reader knowledge, interest, and motivation also matter. Different programs may return different scores because their counting methods differ.

### Chartered Institute of Editing and Proofreading

Practitioner guide: [Editing into Plain English](https://ciep.uk/static/f8b59fff-ebd7-4089-918595de6409fada/Editing-into-Plain-English-CIEP-guide.pdf)

Use the guide to define what the formula misses: headings, logical argument, ambiguity, grammar, punctuation, structure, and usefulness. Do not assess plainness from a formula alone.

## Intentional v1 limitations

Decision recorded: 2026-08-04.

These are accepted tradeoffs, not defects. They match the chosen version 1 behavior and require no further design work now.

1. **The skill affects matching writing tasks, not every AI response.**
   - Revisit when consistent language is needed across unrelated AI responses. A separate platform-level instruction would be a different layer from this skill.
2. **Flesch is an estimate of surface difficulty, not a quality score.**
   - Revisit if results prove too unstable or insufficient for non-native readers. Compare alternative diagnostics or reader testing before adding another score.
3. **Strict source boundaries can limit an explanation without requiring a gap disclaimer.**
   - The skill should answer supported parts directly and mention an omission only when it materially affects the request or would otherwise mislead the user. Revisit if explanations stop too often. Consider a clearly labeled, opt-in outside-context mode.
4. **Tone preservation can limit how aggressively some text is simplified.**
   - Revisit if preserved style repeatedly blocks useful simplification. Consider explicit tone-versus-clarity modes.

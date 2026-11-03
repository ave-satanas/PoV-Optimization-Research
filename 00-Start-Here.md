---
id: optimization-research-index
type: index
status: ready-for-review
created: 2026-11-02
tags: [pov, optimization, research, handoff]
---

# Supplementary optimization research

This is a separate, local research vault for the Path of Valheiman build optimizer. Claude's repository and session were read only. No tests, probes, report generators, mutation gates, game processes, or optimizer imports were run against that repository. Nothing was sent to Claude or published.

## Read in this order

1. [[01-Claude-Handoff]] — prioritized findings and suggested follow-up.
2. [[02-Evaluation-Interpretation]] — why a passive baseline is not a guaranteed floor; legality and precision boundaries.
3. [[03-Optimization-Contract]] — a minimal contract before ranking builds.
4. [[04-Progression-and-Search]] — independent search counterexample and progression requirements.
5. [[05-Regression-Matrix]] — concrete test cases and expected outcomes.
6. [[06-Evidence-and-Reproduction]] — source hashes, scope, and how to reproduce these checks.

## Evidence files

- [Structured finding ledger](evidence/findings.json): identifiers, evidence, confidence, and recommended actions.
- [Independent check results](evidence/checks.json): ten-build checks, eight pair checks, conditional negative rows, and mathematical examples.
- [Source manifest](evidence/source-manifest.json): paths, sizes, SHA-256 hashes, capture time.
- [Read-only analysis script](analysis/research_checks.py): standard library only; does not import the optimizer.

All notes use YAML frontmatter and Obsidian wikilinks. JSON evidence is intended for direct machine ingestion; Markdown carries interpretation. Open this directory as an Obsidian vault; no plugin or configuration is required.

## Evidence boundary

Claude's checkpoint at capture reported **180 tests OK** and an evaluation mutation gate **RUNNING**. Those are Claude's recorded claims, not tests rerun here. The ten-build report and eight comparisons passed the independent consistency checks in this vault. Fifteen negative conditional rows were found in the passive-node table; these are not all necessarily active, obtainable, or part of the community builds.

Source files can be temporary mutation variants. No listed input changed between initial read and hash recheck, but this is not an atomic repository snapshot or a clean-commit audit. Reconfirm implementation observations after Claude's gate finishes. Suggestions describe future work, not changes already applied.

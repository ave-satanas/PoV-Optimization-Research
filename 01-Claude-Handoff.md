---
id: supplementary-handoff
type: handoff
status: ready-for-review
tags: [pov, claude, priorities]
---

# Handoff to Claude

The evaluation milestone is already underway. These findings supplement it; they do not ask for a restart or another mutation run. Finish the active gate before inspecting implementation differences or applying anything here.

| ID | Priority | Finding | Suggested action |
|---|---|---|---|
| R01 | High | “Floor” is not established for every reported stat. Negative conditional modifiers exist. | Describe results as a passive-only baseline; reserve lower-bound language for a proven objective and domain. |
| R02 | High before recommendations | The generic comparison CLI evaluates tracked allocations without returning legality, unlike the corpus report. | Before a consumer recommends a build, attach validation for that exact input/version; keep descriptive comparisons available. |
| R03 | Medium before ranking | Values are rounded before comparison. Tiny displayed differences need not equal rounded raw differences. | Keep report rounding out of the optimization objective; define tolerance and stable tie rules. |
| R04 | Medium before scenario expansion | Comparison compatibility currently checks version and subject list only. | When scenarios/configuration are added, compare a canonical context identity rather than only version/tags. |
| R05 | Medium | The corpus script joins a separately generated validation report by build ID. | Record/check code, tree, rule, and configuration identities before using saved validation as current evidence. |
| R06 | High before “optimal” claims | Cheapest routing solves a different problem from best performance under budget. | Use a small exhaustive value-search oracle and explicit objective before claiming build optimality. |

Detailed reasoning: [[02-Evaluation-Interpretation]], [[03-Optimization-Contract]], [[04-Progression-and-Search]]. Test cases: [[05-Regression-Matrix]]. Machine ledger: [findings.json](evidence/findings.json).

## Positive checks

- All ten saved evaluation costs agree with the corresponding level-D point-check evidence.
- All ten saved legality labels agree with the validation report.
- All eight saved comparison pairs have PASS legality, share the recorded start, and have the correct point delta.
- Three independent mathematical checks pass: early rounding can change a delta; a cheapest route can lose on utility; equal mean hit damage can conceal different lethal outcomes.

These checks establish internal consistency of the captured reports, not in-game accuracy, optimality, or correctness of every stat.

## Small next step

After the current milestone, define one supported scenario and one measurable objective, then validate it exhaustively on a tiny synthetic graph. Keep spell, jewel, and full-gear recommendations blocked where their required mechanics remain unsupported. Do not treat a passive stat count, more nonzero stats, or more expensive allocations as performance evidence.

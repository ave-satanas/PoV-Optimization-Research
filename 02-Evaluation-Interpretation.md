---
id: evaluation-interpretation
type: findings
status: evidence-backed-with-limitations
tags: [pov, evaluation, correctness]
---

# Interpreting passive evaluations

## R01 — Baseline does not imply lower bound

`docs/evaluation.md` calls a value a “floor”; `evaluate.py` and `character.py` use similar language. The actual evaluator disables conditions, supplies live-state values of zero, and omits non-passive sources. This specifies a baseline. It does not prove monotonicity.

The extracted 5.3.6 passive-node table includes:

| Node | Stat | Value | Trigger |
|---|---|---:|---|
| `own10355` | `CostPct` | -0.12 | Airborne |
| `own10373` | `CostPct` | -0.30 | Airborne |
| `own11610` | `ShieldDelayPct` | -0.25 | after Block |
| `own12247` | `ShieldDelayPct` | -0.1875 | FullEitr |

The analysis found 15 negative conditional rows among node mods, excluding mastery-option rows. Turning on such a row can reduce the numerical stat. A lower cost or delay may be useful, which also shows why numerical direction and player benefit are separate questions. Obtainability and active runtime behavior were not checked here.

**Recommendation:** “Calculated passive-only stats under the stated baseline; omitted effects may increase or decrease results.” Do not use this baseline as an admissible search bound without a separate proof for the particular objective. This is an interpretation correction, not evidence that the stat assembly is wrong.

## R02 — Tracking is useful; recommendation requires legality

Observed chain: `tools/compare_builds.py:main` decodes each input and calls `evaluate`, then `compare`. `evaluate` drops missing nodes/unresolved choices and returns stats and cost; it does not call `PassiveTree.legality`. `character.passive_stats` explicitly documents this division. The generic CLI returns neither a path nor a legality outcome.

The corpus generator is different: it attaches level-D evidence from `validation.json`. Its eight captured pairs all pass legality. That distinction should survive downstream consumption.

**Recommendation:** retain descriptive evaluation of invalid historical codes, but require exact-input validation before feeding an allocation to a recommendation/ranking flow. Preserve the original code identity and the dropped-node/choice list. An effective tracked allocation is a different object from the requested allocation when anything was dropped.

Do not silently replace a mandatory mechanic with whatever remains after dropping unresolved choices. This follows the compiler's existing feasibility-first contract.

## R03 — Presentation precision must not define optimization

`evaluate` rounds each stat to six decimal places; `compare` subtracts these rounded values and rounds again.

Independent decimal example:

| Operation | Result |
|---|---:|
| raw A | 0.00000049 |
| raw B | 0.00000051 |
| round(B) − round(A), six decimals | 0.000001 |
| round(B − A), six decimals | 0.000000 |

This is consistent with a display-oriented diff, but would be a weak foundation for ranking nearly equal candidates. Conversely, distinct raw candidates can collapse to an identical report.

**Recommendation:** score before formatting; set a meaningful objective tolerance, then tie-break with a stable canonical allocation/choice order. No request to increase the current report's precision. The existing stat engine already documents a double-versus-float fidelity limit; tolerances should acknowledge measurement/model fidelity as well as serialization precision.

## R04 — Context is part of the result identity

`compare` checks `(version, subjects)` for equality. With the current fixed baseline and ordinary CLI-produced evaluations, this is useful. It is not a complete identity for future condition/configuration-aware comparisons or arbitrary saved dictionaries.

A future context identity should cover data and rules fingerprints, effective configuration, equipment/skills/enemy inputs, live-state assumptions, condition/event state, and model revision. Do not implement unused scenario machinery now. Add identity at the point multiple contexts actually become supported.

Subject-list ordering is currently sorted, but duplicate arguments remain in the output even though `Subjects.of` makes a set. A canonical identity should use sorted unique tags; include a regression case before changing this behavior.

## R05 — Separate report generation needs provenance

`tools/evaluate_corpus.py:run` loads validation by build name, then separately reads the current code and dataset to evaluate it. The inspected join does not verify that the saved validation describes those exact bytes/configuration.

The captured files agree on cost and labels, so this is a stale-artifact risk, not a demonstrated stale report. A future automated consumer should check source identities or compute validation and evaluation within one run. Do not infer freshness from filename or a matching build name alone.

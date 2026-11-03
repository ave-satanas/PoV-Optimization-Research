---
id: regression-matrix
type: test-plan
status: proposed-except-independent-checks
tags: [pov, tests, acceptance]
---

# Regression and research matrix

These are suggested cases for Claude after the active milestone. No new test was added to its repository. Existing coverage may overlap; compare against the final suite before adding tests.

| ID | Case | Expected result | Evidence / scope |
|---|---|---|---|
| T01 | Read captured corpus evaluation and validation | Ten matching legality labels and point totals | **Executed here**, JSON consistency only |
| T02 | Read captured comparison pairs | Eight PASS pairs, valid common start, correct cost delta | **Executed here**, JSON consistency only |
| T03 | Negative conditional `CostPct` row with condition off/on | Numerical value can decrease; no universal lower-bound wording | Data evidence captured; runtime test proposed |
| T04 | Generic comparison of disconnected allocation | Descriptive result allowed; recommendation layer refuses/labels illegal | Proposed boundary test, not an evaluator rewrite |
| T05 | Input code has an unresolved mandatory mastery | Dropped choice remains visible; requirement cannot silently pass | Proposed integration test |
| T06 | 0.00000049 vs 0.00000051 | Early-round delta 0.000001; late-round delta 0 | **Executed here** with Decimal; ranking policy still proposed |
| T07 | Same subjects in different order or duplicated | Canonical context identity is equal | Proposed normalization test |
| T08 | Same version/tags but different config/scenario fingerprint | Refuse a direct comparable-context claim | Proposed for future scenario layer |
| T09 | Same build ID with altered code after saved validation | Stale validation detected before recommending | Proposed provenance test |
| T10 | Same code/version with changed tree or budget config | Prior legality not reused blindly | Proposed provenance test |
| T11 | Cheap mandatory-target route vs higher-value route within budget | Value optimizer matches exhaustive optimum, not cheapest route | Mathematical witness checked; production oracle proposed |
| T12 | Final connected allocation, disconnected first purchase | Reject proposed progression sequence at invalid prefix | Proposed progression test |
| T13 | Option purchase causes budget overflow | Count node cost plus two-step option cost | Proposed integration test; primitive already has cost logic |
| T14 | Required jewel-opened second start | UNKNOWN/unsupported until modelled; no guessed connectivity | Existing Dunin limitation, not newly discovered |
| T15 | Equal mean damage, different lethal tail at health 8 | Keep survival outcomes distinct | **Executed here**, synthetic arithmetic only |
| T16 | A and B have equal scores | Stable tie-break independent of set/hash iteration | Proposed optimizer test |

## Scope of measured checks

The research script asserts report consistency and small mathematical examples. It never imports `pov_opt`, calls .NET probes, generates game data, writes source, or runs a mutation gate. Passing these checks cannot certify the live codebase.

## Evidence to obtain at the desk

Use the project's existing in-game validation protocol rather than starting a parallel game session. For each chosen build/context record exact version and config, code identity, equipment and skill state, conditions, enemy/hit inputs where relevant, and observed versus calculated values. Separate planner tracking/import from actual allocation/export; acceptance by a native reader is not proof of legal or mechanically equivalent allocation.

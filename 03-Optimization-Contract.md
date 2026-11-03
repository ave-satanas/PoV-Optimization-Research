---
id: optimization-contract
type: proposal
status: proposed-not-implemented
tags: [pov, objectives, scenarios]
---

# Minimal contract before ranking

The existing compiler separates interpretation, data, deterministic optimization, and validation. Keep that separation. A stat difference is not an objective function, and more modifiers are not necessarily better.

## One request, explicit constraints

The smallest useful optimization input identifies:

| Field | Why it matters |
|---|---|
| Data version and effective config | Rule-compatible versions can still have different data, tunables, and budgets. |
| Start path and point budget | A legal 350-point build is not a legal 100-point solution. |
| Required mechanics and locked selections | Feasibility must preserve the user's mandatory intent. |
| Available content/items | “Exists in data” does not imply obtainable at the player's progression stage. |
| Supported scenario | Exact weapon/skill/subjects, enemy, conditions, and relevant live-state assumptions. |
| Objective with units | For example damage per supported hit, not a sum of raw stat values. |
| Evidence limits | Unsupported mechanics cannot silently receive a zero score and disappear. |

This is a research checklist for the future spec, not a demand to add eight configuration surfaces immediately.

## Outputs that support a defensible claim

Return feasibility and legality separately from the objective value. Record the evaluated effective allocation, cost, exact assumptions, omitted mechanics, search method, and tie-break. Explain both gained and lost mechanics in a re-optimization.

Use “optimal” only when the defined feasible space was exhausted or a valid bound meets the incumbent. An exact route to selected targets is not proof that those targets are best. A large-tree heuristic should report the best feasible candidate found and, only when available, a valid bound and gap.

For a maximization problem with feasible incumbent L and proven upper bound U, the absolute gap is U − L. A relative gap requires a stated denominator; avoid percentage claims when the denominator is zero or the objective can change sign. No valid bound means no numeric optimality-gap claim.

## Scenarios before averages

Start with one supported, explicit scenario. When multiple scenarios are supported, present per-scenario outcomes before combining them. User-supplied weights express preferences, not mechanical facts; they should never erase hard requirements.

For survival, mean incoming damage alone is insufficient. In a synthetic health-8 example, repeated hits of 5 always leave the player alive after one hit; a 50/50 mixture of 0 and 10 has the same mean of 5 but kills on half of single hits. This does not simulate Valheim mitigation; it demonstrates why “tankier” needs a defined question such as surviving a specified burst, and explicit starting health/shield and timing.

Useful future outputs include damage under named supported inputs, resource demand/sustain where modelled, and survival of named incoming sequences. Do not manufacture spell DPS, minion DPS, or jewel-enhanced survivability from the current passive-only report.

## Pareto comparisons

Candidate A dominates B only within the same feasible domain and complete chosen objective vector: A is no worse on every objective and strictly better on at least one. Keep nondominated alternatives when the user has not chosen a trade-off. An unmodelled dimension prevents a comprehensive dominance claim; it does not count as equality.

Same-start comparison is helpful for path continuity. It does not imply equal budgets, gear, gameplay goals, or stage of progression. The captured `dreng` builds range from 219 to 350 points, so their direct differences describe different investment levels.

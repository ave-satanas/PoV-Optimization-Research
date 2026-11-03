---
id: progression-and-search
type: research
status: mathematical-examples-checked
tags: [pov, optimization, progression, oracle]
---

# Search and progression counterexamples

## R06 — Cheapest routing is not budgeted value search

`PassiveTree.route` minimizes added node cost to hold specified targets. It documents exact Steiner routing for at most eight targets. That is a useful primitive, not a full build optimizer.

Independent synthetic graph (undirected edges):

```text
g -- a -------- t
 \-- b -- c ---/
```

Gate `g` is free. Each other node costs one point. Target `t` is mandatory. Node `t` provides utility 1, node `c` utility 10, and the others utility 0. Budget is 3.

| Allocation | Cost | Utility | Result |
|---|---:|---:|---|
| a, t | 2 | 1 | Cheapest target route |
| b, c, t | 3 | 11 | Best feasible allocation in this example |

The two remaining feasible target-containing triples (`a,b,t` and `a,c,t`) score 1 and 11 respectively; the latter is connected through `t`. Thus the utility optimum is not unique, but every minimum-cost route here loses utility. Stable tie-breaking is required among equal best candidates.

The small self-check verifies that the minimum-cost candidate and a higher-utility feasible candidate differ. It does not invoke or test the optimizer's Steiner implementation. A production oracle should enumerate **all** allocations, not just these candidates.

## Minimal exhaustive oracle for later implementation

Use a tiny graph and enumerate subsets of buyable nodes and supported options. For each candidate: enforce required nodes, validate connectivity from the chosen gate, include extra two-step option costs/conflicts, enforce budget, then evaluate the explicit objective. Choose the best score with a canonical tie-break.

Compare the search engine against this oracle across directed edge cases and small seeded cases. Include tied optima, a negative-value bridge to a valuable target, zero-cost gate, unreachable requirement, two-step choices, unsupported jewel access, and interactions whose benefit is not additive.

Do not use node-local scores as exact subtree values when attribute derivation, conditional effects, conversions, caps, or mastery interactions can change marginal value. Pruning needs a valid bound for those interactions. A baseline described as a floor is not automatically a valid upper bound for maximization.

## A final allocation is not a progression plan

`points_available` depends on level and content awards; it is not simply a fixed multiple of character level. A milestone needs its own available points and acquisition assumptions. The captured compiler contract asks for progression-aware output, but the passive code stores neither gear nor the progression sequence.

For a proposed sequence, validate every prefix from the active gate, not only the final set. Buying `t` first in the graph above is invalid; buying `a` then `t` is connected. Buying a two-step option must include its additional cost at the moment it is selected.

If re-optimization preserves existing nodes, distinguish incremental spend, final spend, and removals/refunds. A cheap route returned with already-held nodes treated as free is not the final budget. An already-held disconnected allocation needs its own validity check.

Before suggesting a respec, show required removals, kept mandatory mechanics, cost/refund assumptions, and any temporarily lost capability. Do not assume intermediate respec states are playable or the refund resource is available.

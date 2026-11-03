---
id: evidence-and-reproduction
type: provenance
status: captured
tags: [pov, evidence, reproducibility]
---

# Evidence and reproduction

## Local sources

Source root:

```text
C:\Users\AveSatanas\Documents\Codex\2026-11-01\referenced-chatgpt-conversation-this-is-an\work\pov-build-optimizer
```

The [manifest](evidence/source-manifest.json) records exact relative paths, bytes, SHA-256 hashes, and UTC capture time. It includes implementation, tests, docs, checkpoint, two reports, and the passive-node table. This vault contains derived findings, not copies of the raw mod tables or full community codes. Do not infer permission to publish the source data from its use in local research.

| Claim | Primary local evidence |
|---|---|
| Fixed baseline, rounding, and context checks | `src/pov_opt/evaluate.py`, `docs/evaluation.md` |
| Generic CLI does not attach legality | `tools/compare_builds.py` call chain |
| Corpus joins separate validation | `tools/evaluate_corpus.py:run` |
| Negative conditional rows | `data/5.3.6/passive_nodes.json` plus extracted identifiers in `checks.json` |
| Routing objective and scope | `src/pov_opt/passives.py:route`, `steiner`, `MAX_TARGETS` |
| Compiler must preserve intent | `docs/nl-build-compiler.md` |
| Current recorded milestone state | `checkpoints/STATUS.json` |

The research used local primary materials only. No internet claims or new external mechanics were introduced. Mathematical examples are labelled as synthetic and do not depend on recalled game behavior.

## Reproduction

From this vault's parent directory, with an available Python 3 interpreter:

```powershell
python -B Optimization-Research/analysis/research_checks.py 'C:\Users\AveSatanas\Documents\Codex\2026-11-01\referenced-chatgpt-conversation-this-is-an\work\pov-build-optimizer'
```

The executed capture used the repository's existing `.venv/Scripts/python.exe` interpreter with `-B`, but ran only this vault's standard-library script. It did not import repository modules. Output writes are confined to this vault's `evidence/` directory. Re-running replaces `checks.json` and `source-manifest.json`; retain a copy if preserving this capture matters.

Expected capture checks: ten builds, eight pairs, fifteen negative conditional node rows, three passing synthetic checks, and no inputs changed during capture. New project versions or reports may change these counts; investigate rather than treating these numbers as permanent acceptance criteria.

## Limitations

- Claude's mutation gate was reported running. Stable hashes during a short read do not prove code is a pristine committed version.
- The capture is not atomic. Reports could theoretically describe different instants even if individual files were stable while read.
- Cost and legality agreement is internal consistency, not independent derivation of game rules.
- No runtime evaluation, Unity/.NET probe, full optimizer test, in-game round trip, or gameplay benchmark was performed.
- No source file, shared report, session, or running process was changed. No message was sent to Claude. The package is ready for the user or a later authorized handoff to supply.

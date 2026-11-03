---
id: repository-readme
type: landing
status: ready-for-review
tags: [pov, research]
---

# Path of Valheiman optimization research

Supplementary research for the Path of Valheiman build optimizer, packaged as an Obsidian vault with Markdown notes and JSON evidence.

**[Start here](00-Start-Here.md)** · [Claude handoff](01-Claude-Handoff.md) · [Findings ledger](evidence/findings.json)

Open this repository's root folder as an Obsidian vault. No plugins are required. Obsidian wikilinks connect the research notes; regular Markdown links connect evidence files.

The research includes interpretation risks, an optimization contract, progression/search examples, and a regression matrix. Its historical capture and limitations are recorded in [Evidence and reproduction](06-Evidence-and-Reproduction.md). Statements about work not yet published describe the original research session, before this repository was created.

To refresh the independent checks with Python 3, from the repository root:

```text
python -B analysis/research_checks.py <path-to-pov-build-optimizer>
```

This replaces the evidence capture. It reads source/report files without importing optimizer code and writes only this vault's evidence. It does not certify gameplay accuracy or run the optimizer's test suite.

---
type: Playbook
id: https://w3id.org/lmodel/void/knowledge/playbooks/update-upstream-pins
genre: how-to
title: Update the upstream pins
description: "What to do when the upstream watch opens an issue: a new edition of the VoID Note, a changed or dropped vocabulary file, a changed licence, or a check that could not finish; which pins move together (the watch, `scripts/extract_void_terms.py`, the schema header and the term lists' checksums)."
sources:
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring, the pins and the report lines
  - id: extract
    resource: scripts/extract_void_terms.py
    title: the docstring
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: TERM_LISTS and the pin tests
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Update the upstream pins

The upstream watch opens or updates one issue when a check needs a person.[^watch]

- **A new edition of the Note.** Read what changed and decide whether the schema moves to it. If it does, move `PINNED_EDITION` and `PINNED_SOURCE` in `scripts/check_upstream_release.py` and the schema header's `version` and `source` together.
- **The vocabulary file changed or is gone.** Move `PINNED_COMMIT` and `PINNED_BLOBS` in the watch and `VOID_COMMIT` and `VOID_BLOB` in `scripts/extract_void_terms.py`, then run `uv run scripts/extract_void_terms.py`, which refuses any file but the pinned one.[^extract] Move the lists' checksums in `tests/test_upstream.py`'s `TERM_LISTS`, and change the schema where a term changed.[^test_upstream.py]
- **A licence changed.** Read what the new terms allow, and update NOTICE.
- **A check could not finish.** Run the watch again; a refused or cut-off request says nothing about the upstream.

`just test` holds the header, both scripts' pins and the lists equal.

[^watch]: scripts/check_upstream_release.py, the docstring
[^extract]: scripts/extract_void_terms.py, the docstring
[^test_upstream.py]: tests/test_upstream.py, TERM_LISTS

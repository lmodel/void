---
type: Policy
id: https://w3id.org/lmodel/void/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The rules for AI-assisted work on void: a contributor owns what they submit, an element must say what VoID says, no text of the Note or the vocabulary file, VoID's terms keep VoID's IRIs, and the scheduled librarian commits as a bot, through pull requests a person approves."
resource: AI_COVENANT.md
sources:
  - id: covenant
    resource: AI_COVENANT.md
    title: the project note and Repository-Owned Agent Automation
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` makes a contributor the author of whatever they submit, whatever tools helped. Its note for this project names two risks: a term or rule a model produced, presented as VoID's, and copied text of the Note or the vocabulary file. So every element with a `void:` IRI names a term of the pinned vocabulary file, and nothing copies or closely paraphrases either text. VoID's terms keep VoID's IRIs, and only the schema's additions sit under `void_linkml:`.[^covenant]

The scheduled `knowledge-librarian` agent commits as `knowledge-librarian[bot]`, opens a pull request a person must approve, holds no write token in its own job, and never writes a person's confirmation.[^covenant]

[^covenant]: AI_COVENANT.md, the project note and Repository-Owned Agent Automation

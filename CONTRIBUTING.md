# Contributing to void

*This file is a checklist, not a design log. Each rule is a line or two that links to where its reasoning lives: a code comment, a workflow header, or a linked page. `lint-and-docs.yaml` holds the file to a word budget so it stays that way.*

## What this project is

A LinkML schema of the Vocabulary of Interlinked Datasets (VoID), as the W3C Interest Group Note of 3 March 2011 explains it. A knowledge bundle can type its concepts with its classes. The schema keeps VoID's names and IRIs and carries none of VoID's text; [NOTICE](NOTICE) says why.

| Path | Holds |
| --- | --- |
| `src/void/schema/void.yaml` | The LinkML schema. Edit this. |
| `src/void/datamodel/`, `project/`, `docs/schema/` | Artefacts generated from the schema. |
| `docs/` | The website's own pages. |
| `tests/` | Python tests, example data and the upstream term lists. |
| `.lokf/knowledge/` | This repository's knowledge bundle. |

## Development setup

You need Python 3.10+, [uv](https://docs.astral.sh/uv/) and [just](https://github.com/casey/just).

```bash
git clone https://github.com/lmodel/void.git
cd void
uv sync --group dev
just --list
```

### Agent skills (optional, only for this repo's `.lokf/` bundle)

The bundle is maintained with the Knowledge Trust Ladder (KTL) skills, **installed, never committed**. Continuous integration (CI) installs the librarian skill at run time, pinned to a release. [The install page](https://w3id.org/ktl/docs/install/) lists every route. With npm:

```bash
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-librarian --yes   # derive concepts
npx skills add noelmcloughlin/knowledge-trust-ladder --skill ktl-curator --yes     # confirm them as a person
```

## Before opening a pull request

- **Edit the schema, then regenerate.** Edit `src/void/schema/void.yaml`, run `just gen-project`, `just gen-doc` and `just lokf-adapt`, and commit the output. `project/`, `src/void/datamodel/`, `docs/schema/` and `.lokf/void.yaml` are generated.
- **Keep VoID's names and IRIs**, and those of the Dublin Core, FOAF and RDF Schema terms. `tests/test_upstream.py` holds the schema to `tests/upstream/void-terms.tsv`, which `scripts/extract_void_terms.py` writes from the pinned vocabulary file. A mapping names a term the pinned term lists hold; a term with no sure match stays unmapped.
- **Carry none of VoID's text.** No definition, comment or example from the Note or the vocabulary file goes anywhere here, copied or closely paraphrased. Cite the section or the term in the pull request. [NOTICE](NOTICE) states the position; [AI_COVENANT.md](AI_COVENANT.md) says why.
- **Render the pinned edition.** The schema header and `scripts/check_upstream_release.py` name the same edition, and `tests/test_upstream.py` holds them equal.
- **Keep names apart.** A host imports this adapt copy beside the Linked Open Knowledge Format (LOKF) schema and the released neighbours' copies in `tests/neighbours/`, so a shared name carries one Internationalized Resource Identifier (IRI). `tests/test_schema_rules.py` checks this.
- **Run the tests**: `just test` (schema generation, `pytest` and the examples under `tests/data/`). Example data goes in `tests/data/valid/` and `tests/data/invalid/`, named `ClassName-suffix.yaml`; an invalid example's first line, `# Fails at: <pointer>`, names where it fails.
- **Follow the schema's conventions**: VoID's own names (PascalCase classes, lowerCamelCase properties), each identifier a top-level slot listed first in its class, a short description on every element. `just lint` checks, under `.linkmllint.yaml`.
- **Run the pre-commit hooks** on what you staged (`uvx pre-commit run`), keep changes focused and fill in the pull request template.
- **Lock files are part of the change.** CI installs with `uv sync --locked`, so an edit without its `uv.lock` (or `.lokf/uv.lock`) fails.
- **Knowledge-bundle changes**: `cd .lokf && just lokf-validate` must pass, and `knowledge-registrar.yaml` runs on any `.lokf/**` change.
- **`lint-and-docs.yaml` is easy to trip locally**: ShellCheck, actionlint, markdownlint, lychee and codespell, under the configs in the root.
- **Actions are pinned to commit hashes**, with the version in a trailing comment; Dependabot bumps them.
- **The skills pin moves with the sidecar copies.** When moving `TRUST_LADDER_SKILLS_REF` in `.github/workflows/knowledge-librarian.yaml`, copy the other `knowledge-*.yaml` workflows and `.lokf/scripts/` and `.lokf/m365/` from that release's `skills/ktl-sidecar/templates/` in the same pull request.
- **If your change alters behaviour**, add an entry under `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md).

## Code of conduct

Participation here is covered by the [Contributor Covenant](CODE_OF_CONDUCT.md).

## Using AI tools

Artificial intelligence (AI) assistance is welcome; [AI_COVENANT.md](AI_COVENANT.md) sets the rules, for people and the scheduled `knowledge-librarian` agent alike. A model's text must not reproduce the Note's wording.

## Reporting issues

Use the [issue tracker](https://github.com/lmodel/void/issues) for the schema. A problem in VoID itself belongs with [its editors](https://github.com/cygri/void/issues).

## Releasing (maintainers)

- Write `## [Unreleased]` in [CHANGELOG.md](CHANGELOG.md) as you go. The release job refuses an empty one (`.github/scripts/changelog-release.mjs check`).
- Type the commit ([Conventional Commits](https://www.conventionalcommits.org/)) for what the change *is*. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release. Other types leave their entries for the next release that does. A pull request that would release must carry a releasing type in its title too, since a squash merge takes its subject from it.
- On merge, [`semantic-release.yml`](.github/workflows/semantic-release.yml) retitles the section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches `.github/workflows/knowledge-release.yaml`, which attaches the schema copy and the bundle when the bundle or the schema changed.
- That step runs behind the `release` GitHub Environment. Configure required reviewers on it in Settings → Environments, or every qualifying merge is released unattended.
- Below 1.0.0: push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0. Both release jobs refuse to run without a `v*` tag, because semantic-release would otherwise start at 1.0.0. `.releaserc.json` maps `breaking: true` to `minor`, and reaching 1.0.0 means removing that rule in a pull request of its own.
- A branch rule requiring pull requests, status checks or signed commits would reject the release job's own push to `main`, so leave them off. [SECURITY.md](SECURITY.md) says what holds `main` instead, and the shared design is on [KTL's releasing page](https://github.com/noelmcloughlin/knowledge-trust-ladder/blob/main/docs/releasing.md).

## License

By contributing, you agree that your contributions are licensed under the [Apache License 2.0](LICENSE). VoID's Note and vocabulary file are under their own terms; [NOTICE](NOTICE) says what they allow. Update it when you add something from elsewhere.

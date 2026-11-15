---
type: Service
id: https://w3id.org/lmodel/void/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The knowledge website in `website/`, a Hugo site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/void/`: the README as its home page, `docs/`, the schema's pages, a page per concept and the four `lokf export` files, with redirects from the retired mkdocs site's addresses."
resource: website
sources:
  - id: website-readme
    resource: website/README.md
    title: the list of what the site shows, and Preview it
  - id: site-config
    resource: website/site.toml
    title: the site's address, title and redirects
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:10:46Z"
status: draft
---

# Documentation site

`website/` builds the site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/void/`. The site shows:

- the README as its home page;
- each page under `docs/` as a page under `docs/`;
- each schema page that `gen-doc` writes as a page under `schema/`;
- each concept as a page under `knowledge/`, beside the four files `lokf export` writes.[^website-readme]

`website/scripts/build.sh` builds it into `website/dist/` with Hugo and Pagefind, then checks every link between its pages. It needs bash, git and uv.[^website-readme]

`site.toml` redirects the retired mkdocs site's addresses: each old element page at the site's root and under `/elements/` to its successor's schema page, or to the schema's index where none exists, and `/about` to `/docs/about/`.[^site-config]

[^website-readme]: website/README.md, the list of what the site shows, and Preview it
[^site-config]: website/site.toml, the site's address, title and redirects

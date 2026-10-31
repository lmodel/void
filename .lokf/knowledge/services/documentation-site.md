---
type: Service
id: https://w3id.org/lmodel/void/knowledge/services/documentation-site
genre: reference
title: Documentation site
description: "The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/void/`: the README as its home page, `docs/`, the schema's pages, a page per concept and the four `lokf export` files, with redirects from the retired mkdocs site's addresses."
resource: website
sources:
  - id: website-readme
    resource: website/README.md
    title: the list of what the site shows
  - id: site-config
    resource: website/site.config.mjs
    title: REPO, SITE, BASE, DOCS and REDIRECTS
generated:
  by: process:ktl-librarian
  at: "2026-10-31T15:05:26Z"
status: draft
---

# Documentation site

`website/` builds the site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/void/`. The README is its home page, each page under `docs/` a page under `docs/`, each schema page that `gen-doc` writes a page under `schema/`, and each concept a page under `knowledge/`, beside the four files `lokf export` writes.[^website-readme] `cd website && npm ci --ignore-scripts && npm run build` builds it and checks every link.

`site.config.mjs` redirects the retired mkdocs site's addresses: each old element page at the site's root and under `/elements/` to its successor's schema page, or to the schema's index where none exists, and `/about` to `/docs/about/`.[^site-config]

[^website-readme]: website/README.md, the list of what the site shows
[^site-config]: website/site.config.mjs, DOCS and REDIRECTS

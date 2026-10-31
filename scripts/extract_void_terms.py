#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["rdflib>=7.1"]
# ///
"""List the terms of VoID and of the vocabularies the schema names beside it.

The schema renders the Vocabulary of Interlinked Datasets (VoID) with VoID's
own names and IRIs, and names terms of five other vocabularies: Dublin Core
and FOAF properties as slot IRIs, as the VoID Note uses them, and FOAF,
SPARQL Service Description and DCAT classes in its mappings. The tests check
the schema against two term lists this script writes, so that no IRI is
invented and no VoID term is left out:

- tests/upstream/void-terms.tsv holds each term VoID's vocabulary file
  declares, with the facts the file states about it: its kind, whether it is
  functional, its domain, its range and its parent. It holds no label or
  comment, which are the file's text.
- tests/upstream/vocabulary-terms.txt holds each class and property the five
  other vocabularies' published files declare in their own namespaces.

The script downloads each file into memory, refuses it unless it is the
pinned one (VoID's file by its git object hash at the editors' pinned commit,
the others by their SHA-256), and writes the lists, sorted. Nothing else is
written. Usage::

    uv run scripts/extract_void_terms.py [OUTPUT_DIR]

OUTPUT_DIR defaults to tests/upstream. When a pinned file moves, move its pin
here and in scripts/check_upstream_release.py, rerun this script, and move
the term lists' checksums in tests/test_upstream.py.
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from pathlib import Path

from rdflib import OWL, RDF, RDFS, Graph, URIRef

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "tests" / "upstream"
USER_AGENT = "lmodel-void-watch"
MAX_BYTES = 5_000_000

# VoID's vocabulary file, as its editors keep it, at the commit and with the
# git object hash scripts/check_upstream_release.py pins.
VOID = "http://rdfs.org/ns/void#"
VOID_COMMIT = "5b2ca68b7897c2613d4269fd725f1812dce21267"
VOID_PATH = "rdfs/void.ttl"
VOID_BLOB = "9a7ca133acf83628d7850b0bdff58c507a5504d4"
VOID_URL = f"https://raw.githubusercontent.com/cygri/void/{VOID_COMMIT}/{VOID_PATH}"

# The other vocabularies, each by its prefix, its namespace, the address of
# its published file, the file's syntax and the file's SHA-256 as read on
# 2026-10-31.
VOCABULARIES = (
    (
        "dcterms",
        "http://purl.org/dc/terms/",
        "https://www.dublincore.org/specifications/dublin-core/dcmi-terms/dublin_core_terms.ttl",
        "turtle",
        "13df401072dd7015bf9d75162f3e41c8138075304b7b9cc1aa1e9c16db976797",
    ),
    (
        "foaf",
        "http://xmlns.com/foaf/0.1/",
        "https://xmlns.com/foaf/spec/index.rdf",
        "xml",
        "3d859b5d92a2c3d041545d014fa826f682ca06d056af8c7b31e32d930abf2bc5",
    ),
    (
        "rdfs",
        "http://www.w3.org/2000/01/rdf-schema#",
        "https://www.w3.org/2000/01/rdf-schema.ttl",
        "turtle",
        "ecee3a011b7c13ea2a7e40b0a208bfe6be53d69fdd53ee035e09e9f9e5108ad6",
    ),
    (
        "sd",
        "http://www.w3.org/ns/sparql-service-description#",
        "https://www.w3.org/ns/sparql-service-description.ttl",
        "turtle",
        "a4e4ab035c909d4aeb140ab5807a3b49dfa0ecee587dc9109214ecfaff712878",
    ),
    (
        "dcat",
        "http://www.w3.org/ns/dcat#",
        "https://www.w3.org/ns/dcat3.ttl",
        "turtle",
        "d1624d3bbf364f6fc1d43b9a188bbb9e67639b1a7d46a5cb7ea3f5d47d02b62f",
    ),
)

CLASS_TYPES = (RDFS.Class, OWL.Class)
PROPERTY_TYPES = (
    RDF.Property,
    OWL.ObjectProperty,
    OWL.DatatypeProperty,
    OWL.AnnotationProperty,
    OWL.FunctionalProperty,
)


def fetch(url: str) -> bytes:
    """A file's bytes, read into memory and capped at MAX_BYTES."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read(MAX_BYTES + 1)
    if len(data) > MAX_BYTES:
        raise SystemExit(f"{url}: larger than {MAX_BYTES} bytes")
    return data


def blob_sha(data: bytes) -> str:
    """Git's object hash of a file's bytes."""
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def kind(graph: Graph, term: URIRef) -> str | None:
    types = set(graph.objects(term, RDF.type))
    if types & set(CLASS_TYPES):
        return "Class"
    if types & set(PROPERTY_TYPES):
        return "Property"
    return None


def _joined(graph: Graph, term: URIRef, predicate: URIRef) -> str:
    return " ".join(sorted(str(o) for o in graph.objects(term, predicate)))


def void_rows(graph: Graph) -> list[str]:
    """One tab-separated line per VoID term: the term, its kind, whether it
    is functional, and its domain, range and parent, each an IRI or empty."""
    rows = []
    for term in sorted({s for s in graph.subjects() if isinstance(s, URIRef)}):
        if not str(term).startswith(VOID):
            continue
        what = kind(graph, term)
        if what is None:
            continue
        functional = (term, RDF.type, OWL.FunctionalProperty) in graph
        parent = RDFS.subClassOf if what == "Class" else RDFS.subPropertyOf
        rows.append(
            "\t".join(
                [
                    str(term),
                    what,
                    "true" if functional else "false",
                    _joined(graph, term, RDFS.domain),
                    _joined(graph, term, RDFS.range),
                    _joined(graph, term, parent),
                ]
            )
        )
    return rows


def main(argv: list[str]) -> int:
    output = Path(argv[0]) if argv else OUTPUT
    data = fetch(VOID_URL)
    if blob_sha(data) != VOID_BLOB:
        raise SystemExit(f"{VOID_URL}: got blob {blob_sha(data)}, pinned {VOID_BLOB}")
    graph = Graph().parse(data=data, format="turtle")
    modified = next(
        graph.objects(
            URIRef("http://vocab.deri.ie/void"),
            URIRef("http://purl.org/dc/terms/modified"),
        )
    )
    rows = void_rows(graph)
    head = [
        f"# The terms VoID's vocabulary file declares: {VOID_PATH} in cygri/void at commit {VOID_COMMIT},",
        f"# git object {VOID_BLOB}, modified {modified}. Written by scripts/extract_void_terms.py.",
        "# term\tkind\tfunctional\tdomain\trange\tparent",
    ]
    output.mkdir(parents=True, exist_ok=True)
    (output / "void-terms.tsv").write_text(
        "\n".join(head + rows) + "\n", encoding="utf-8"
    )

    head, terms = (
        ["# Classes and properties of the vocabularies the schema names beside VoID."],
        set(),
    )
    for prefix, namespace, url, syntax, sha256 in VOCABULARIES:
        data = fetch(url)
        digest = hashlib.sha256(data).hexdigest()
        if digest != sha256:
            raise SystemExit(f"{url}: got SHA-256 {digest}, pinned {sha256}")
        head.append(f"# {prefix} {namespace} from {url}, SHA-256 {sha256}.")
        theirs = Graph().parse(data=data, format=syntax)
        for term in {s for s in theirs.subjects() if isinstance(s, URIRef)}:
            what = kind(theirs, term)
            if what and str(term).startswith(namespace) and str(term) != namespace:
                terms.add(f"{term}\t{what}")
    head.append("# Written by scripts/extract_void_terms.py.")
    (output / "vocabulary-terms.txt").write_text(
        "\n".join(head + sorted(terms)) + "\n", encoding="utf-8"
    )
    print(f"{len(rows)} VoID terms and {len(terms)} other terms written to {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

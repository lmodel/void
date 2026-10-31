"""Checks that the schema renders the VoID edition and terms the pins name.

Nothing of VoID is copied here. scripts/check_upstream_release.py pins the
Note's edition and the editors' vocabulary file, and
scripts/extract_void_terms.py wrote two term lists from pinned files:
tests/upstream/void-terms.tsv, VoID's terms with the facts the vocabulary
file states about each, and tests/upstream/vocabulary-terms.txt, the terms
of the other vocabularies the schema names. These tests read the lists
offline and hold the schema header, the pins and the schema's terms to them.
"""

import hashlib
import importlib.util
from pathlib import Path

import pytest
import yaml
from linkml_runtime import SchemaView

ROOT = Path(__file__).parent.parent
SCHEMA = ROOT / "src" / "void" / "schema" / "void.yaml"
UPSTREAM = Path(__file__).parent / "upstream"
VOID_TERMS = UPSTREAM / "void-terms.tsv"
OTHER_TERMS = UPSTREAM / "vocabulary-terms.txt"

# The term lists as scripts/extract_void_terms.py wrote them. Move these
# with the lists when a pinned file moves.
TERM_LISTS = {
    "void-terms.tsv": "57fca7297cc96a366f786083a62bcda21414fa13fca6781c6bbe2232e6aecc97",
    "vocabulary-terms.txt": "ba775b3f2a08c45a328dcb67c429805d82e9d75f23e4e3745062be06702c62a5",
}

VOID = "http://rdfs.org/ns/void#"
XSD = "http://www.w3.org/2001/XMLSchema#"
RDFS = "http://www.w3.org/2000/01/rdf-schema#"
RDF = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
FOAF = "http://xmlns.com/foaf/0.1/"

# How the schema writes each range the vocabulary file states: a datatype as
# a LinkML type, a VoID class as a class of this schema, and a class or
# property whose instances are named by IRI as a uri or a CURIE. A property
# with no range takes an IRI.
TYPE_FOR_RANGE = {
    f"{XSD}integer": "integer",
    f"{RDFS}Literal": "string",
    f"{RDFS}Class": "uriorcurie",
    f"{RDF}Property": "uriorcurie",
    f"{RDFS}Resource": "uri",
    f"{FOAF}Document": "uri",
    "": "uri",
}

# The one property with no range in the vocabulary file whose value the
# Note's section 4.2 makes a literal: a regular expression.
LITERAL_WITHOUT_A_RANGE = {f"{VOID}uriRegexPattern"}

# VoID's sub-properties that the schema cannot make LinkML sub-slots: a
# class or property partition is a value inside its dataset here, while
# subset names another dataset by its IRI, so the two ranges differ.
NOT_A_SUB_SLOT = {f"{VOID}classPartition", f"{VOID}propertyPartition"}


def _load(module_name, path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


WATCH = _load("watch_pins", ROOT / "scripts" / "check_upstream_release.py")
SV = SchemaView(str(SCHEMA))


def _rows(path):
    return [
        line.split("\t")
        for line in path.read_text().splitlines()
        if not line.startswith("#")
    ]


def void_terms():
    """Each VoID term the vocabulary file declares, by its IRI."""
    return {
        term: {
            "kind": kind,
            "functional": functional == "true",
            "domain": domain,
            "range": range_,
            "parent": parent,
        }
        for term, kind, functional, domain, range_, parent in _rows(VOID_TERMS)
    }


def other_terms():
    return {term: kind for term, kind in _rows(OTHER_TERMS)}


def _iri(curie):
    return SV.expand_curie(curie)


def _classes_by_iri():
    return {_iri(c.class_uri): c.name for c in SV.all_classes().values()}


def _slots_by_iri():
    return {_iri(s.slot_uri): s.name for s in SV.all_slots().values() if s.slot_uri}


def test_the_term_lists_are_the_pinned_ones():
    """Each term list is the file the extract script wrote, byte for byte."""
    for name, sha256 in TERM_LISTS.items():
        digest = hashlib.sha256((UPSTREAM / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_the_header_names_the_pinned_edition():
    """The header's version and source are the edition the watch pins, and
    its annotations name the pinned vocabulary file."""
    header = yaml.safe_load(SCHEMA.read_text())
    assert str(header["version"]) == WATCH.PINNED_EDITION
    assert header["source"] == WATCH.PINNED_SOURCE
    assert WATCH.edition_of(WATCH.PINNED_SOURCE) == WATCH.PINNED_EDITION
    assert header["license"] == "Apache-2.0"
    annotations = header["annotations"]
    path = next(iter(WATCH.PINNED_BLOBS))
    assert annotations["vocabulary_file"] == (
        f"https://github.com/cygri/void/blob/{WATCH.PINNED_COMMIT}/{path}"
    )
    assert WATCH.PINNED_DOCUMENT_LICENSE in annotations["upstream_license"]
    assert f"modified {annotations['vocabulary_modified']}." in VOID_TERMS.read_text()


def test_the_extract_script_and_the_watch_pin_the_same_file():
    """Both scripts name the same commit and git object for the vocabulary
    file, and the term list says it was read from them."""
    extract = _load("extract_pins", ROOT / "scripts" / "extract_void_terms.py")
    assert extract.VOID_COMMIT == WATCH.PINNED_COMMIT
    assert {extract.VOID_PATH: extract.VOID_BLOB} == WATCH.PINNED_BLOBS
    head = VOID_TERMS.read_text()
    assert f"at commit {WATCH.PINNED_COMMIT}," in head
    assert f"git object {extract.VOID_BLOB}," in head
    for prefix, namespace, url, _syntax, sha256 in extract.VOCABULARIES:
        assert (
            f"# {prefix} {namespace} from {url}, SHA-256 {sha256}."
            in OTHER_TERMS.read_text()
        )


def test_every_void_term_is_rendered_and_no_other():
    """Each class and property VoID declares is a class or slot of the schema
    with its IRI, and every element under VoID's namespace is one of them."""
    terms = void_terms()
    classes, slots = _classes_by_iri(), _slots_by_iri()
    for term, facts in terms.items():
        found = classes if facts["kind"] == "Class" else slots
        assert term in found, term
    rendered = {i for i in list(classes) + list(slots) if i.startswith(VOID)}
    assert rendered == set(terms)


def test_each_class_keeps_its_parent():
    """A VoID subclass is the schema's subclass, and a parent outside VoID is
    the class's broad mapping."""
    classes = _classes_by_iri()
    for term, facts in void_terms().items():
        if facts["kind"] != "Class" or not facts["parent"]:
            continue
        cls = SV.get_class(classes[term])
        if facts["parent"].startswith(VOID):
            assert cls.is_a == classes[facts["parent"]], term
        else:
            assert facts["parent"] in {_iri(m) for m in cls.broad_mappings}, term


def _domain_classes(domain):
    """The classes a slot of this domain may sit on: the class with the
    domain's IRI, its descendants, and a class whose broad mapping it is."""
    names = set()
    for cls in SV.all_classes().values():
        iris = {_iri(cls.class_uri)} | {_iri(m) for m in cls.broad_mappings}
        if domain in iris:
            names |= {cls.name} | set(SV.class_descendants(cls.name))
    return names


def _users(slot_name):
    return {c for c in SV.all_classes() if slot_name in SV.class_slots(c)}


@pytest.mark.parametrize(
    "term", sorted(t for t, f in void_terms().items() if f["kind"] == "Property")
)
def test_each_property_keeps_its_domain_range_and_cardinality(term):
    """A VoID property sits only on classes of its domain, has the range the
    vocabulary file gives, is single-valued where VoID calls it functional,
    and is a sub-slot of its parent property."""
    facts = void_terms()[term]
    name = _slots_by_iri()[term]
    users = _users(name)
    assert users, term
    assert users <= _domain_classes(facts["domain"]), (term, users)
    for user in users:
        slot = SV.induced_slot(name, user)
        if facts["range"].startswith(VOID):
            range_class = SV.get_class(slot.range)
            iris = {_iri(range_class.class_uri)} | {
                _iri(m) for m in range_class.broad_mappings
            }
            assert facts["range"] in iris, (term, user, slot.range)
        elif term in LITERAL_WITHOUT_A_RANGE:
            assert slot.range == "string", (term, user, slot.range)
        else:
            assert slot.range == TYPE_FOR_RANGE[facts["range"]], (
                term,
                user,
                slot.range,
            )
        if facts["functional"]:
            assert not slot.multivalued, (term, user)
    slot = SV.get_slot(name)
    if facts["parent"] and term not in NOT_A_SUB_SLOT:
        assert _iri(SV.get_slot(slot.is_a).slot_uri) == facts["parent"], term
    elif not facts["parent"]:
        assert slot.is_a is None, term


def _mapping_iris(element):
    for key in (
        "exact_mappings",
        "close_mappings",
        "related_mappings",
        "narrow_mappings",
        "broad_mappings",
    ):
        for curie in getattr(element, key) or []:
            yield curie


def test_every_other_term_is_one_its_vocabulary_declares():
    """Each slot IRI outside VoID and this schema names a property, and each
    mapping a class, that its vocabulary's pinned file declares, under a
    prefix the schema binds. A mapping into VoID names one of VoID's classes."""
    others, terms = other_terms(), void_terms()
    own = SV.schema.prefixes[SV.schema.default_prefix].prefix_reference
    for slot in SV.all_slots().values():
        iri = _iri(slot.slot_uri) if slot.slot_uri else None
        if iri and not iri.startswith((VOID, own)):
            assert others.get(iri) == "Property", (slot.name, iri)
    mapped = 0
    for cls in SV.all_classes().values():
        for curie in _mapping_iris(cls):
            prefix, sep, _ = curie.partition(":")
            assert sep and prefix in SV.schema.prefixes, curie
            iri = _iri(curie)
            if iri.startswith(VOID):
                assert terms[iri]["kind"] == "Class", (cls.name, curie)
            else:
                assert others.get(iri) == "Class", (cls.name, curie)
            mapped += 1
    assert mapped

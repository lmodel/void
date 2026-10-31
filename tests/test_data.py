"""Checks the example data against the schema and its generated models.

Every valid example must load and validate, and every counter-example must
fail at the place its first line names. The examples under
tests/data/problem/valid/ hold the `class` key of a class partition, which
is a Python keyword: the generated dataclasses cannot load it under LinkML
1.12.1, so those examples are validated and loaded through the Pydantic
model, which aliases the key, but not through the dataclasses or the
example runner. tests/data/README.md says the same.
"""

import json
import re
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader

import void.datamodel.void
import void.datamodel.void_pydantic

ROOT = Path(__file__).parent.parent
DATA = Path(__file__).parent / "data"
SCHEMA = ROOT / "src" / "void" / "schema" / "void.yaml"
COMMITTED_JSON_SCHEMA = ROOT / "project" / "jsonschema" / "void.schema.json"

LOADABLE = sorted((DATA / "valid").glob("*.yaml"))
KEYWORD_KEYED = sorted((DATA / "problem" / "valid").glob("*.yaml"))
VALID = LOADABLE + KEYWORD_KEYED
INVALID = sorted((DATA / "invalid").glob("*.yaml"))


def _class(path):
    return path.stem.split("-")[0]


def _load(path):
    return yaml.safe_load(path.read_text())


@pytest.mark.parametrize("path", LOADABLE, ids=lambda p: p.name)
def test_valid_examples_load_as_dataclasses(path):
    """An example loads into the generated dataclass its file name names."""
    target = getattr(void.datamodel.void, _class(path))
    assert yaml_loader.load(str(path), target_class=target)


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_valid_examples_load_as_pydantic(path):
    """An example loads into the generated Pydantic class, `class` key and all."""
    target = getattr(void.datamodel.void_pydantic, _class(path))
    assert target.model_validate(_load(path))


# The JSON Schema the validator generates is the one check that applies every
# constraint the schema states (docs/index.md lists them, and what the
# generated models leave out), so each example is held to it.
@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_valid_examples_validate(path):
    """Every valid example passes the validator."""
    report = validate(_load(path), str(SCHEMA), _class(path))
    assert not report.results, [r.message for r in report.results]


def _fails_at(path):
    first = path.read_text().splitlines()[0]
    assert first.startswith("# Fails at: "), (
        f"{path.name}: the first line names where it fails, as # Fails at: /key"
    )
    return first.removeprefix("# Fails at: ").strip()


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.name)
def test_counter_examples_fail_where_they_say(path):
    """Every counter-example fails the validator at the place its first line
    names, as `# Fails at: <JSON pointer>`, and nowhere else, so a file that
    starts failing for another reason fails this test."""
    pointer = _fails_at(path)
    report = validate(_load(path), str(SCHEMA), _class(path))
    messages = [r.message for r in report.results]
    assert messages, f"{path.name} passed the validator"
    assert all(m.endswith(f" in {pointer}") for m in messages), messages


def _committed_errors(instance, class_name):
    definitions = json.loads(COMMITTED_JSON_SCHEMA.read_text())["$defs"]
    schema = {"$ref": f"#/$defs/{class_name}", "$defs": definitions}
    validator = jsonschema.Draft202012Validator(
        schema, format_checker=jsonschema.FormatChecker()
    )
    return list(validator.iter_errors(instance))


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_valid_examples_pass_the_committed_json_schema(path):
    """The committed project/jsonschema file accepts every valid example, so
    it is the schema's current rendering."""
    assert not _committed_errors(_load(path), _class(path))


def _pointer(error):
    return "/" + "/".join(str(part) for part in error.absolute_path)


@pytest.mark.parametrize("path", INVALID, ids=lambda p: p.name)
def test_counter_examples_fail_the_committed_json_schema(path):
    """The committed project/jsonschema file refuses every counter-example at
    the place its first line names, as the validator does."""
    errors = _committed_errors(_load(path), _class(path))
    assert errors, f"{path.name} passed the committed JSON Schema"
    assert {_pointer(e) for e in errors} == {_fails_at(path)}, [e.message for e in errors]


def test_every_class_has_an_example():
    """Each class has a valid example: a concept may name four of them as its
    type, and the partitions are values those hold."""
    classes = set(yaml.safe_load(SCHEMA.read_text())["classes"])
    examples = {_class(p) for p in VALID}
    assert classes <= examples, sorted(classes - examples)


# The rules no validator states, held over every valid example. docs/index.md
# lists them, and the schema's comments say why each is out of the
# validator's reach.


def linkset_faults(record):
    """What breaks VoID's rule that a linkset links two distinct datasets: the
    targets, the subjects' target and the objects' target together name
    exactly two, the subjects' and the objects' target differ, and each is one
    of the targets where those are given."""
    faults = []
    targets = list(record.get("target") or [])
    directed = [record.get(k) for k in ("subjectsTarget", "objectsTarget")]
    named = set(targets) | {d for d in directed if d}
    if len(named) != 2:
        faults.append(f"names {len(named)} distinct datasets, not two")
    if len(targets) != len(set(targets)):
        faults.append("repeats a target")
    if all(directed) and directed[0] == directed[1]:
        faults.append("has one dataset as both its subjects' and its objects' target")
    if targets and any(d and d not in targets for d in directed):
        faults.append(
            "has a subjects' or objects' target that is not one of its targets"
        )
    return faults


def pattern_faults(record):
    """What breaks a dataset's URI patterns: its uriRegexPattern compiles,
    and each example and root resource starts with its uriSpace and matches
    its uriRegexPattern, where it states them."""
    faults = []
    pattern = record.get("uriRegexPattern")
    if pattern is not None:
        try:
            compiled = re.compile(pattern)
        except re.error as err:
            return [f"uriRegexPattern does not compile: {err}"]
    space = record.get("uriSpace")
    resources = (record.get("exampleResource") or []) + (
        record.get("rootResource") or []
    )
    for resource in resources:
        if space and not resource.startswith(space):
            faults.append(f"{resource} does not start with the uriSpace")
        if pattern is not None and not compiled.search(resource):
            faults.append(f"{resource} does not match the uriRegexPattern")
    return faults


@pytest.mark.parametrize("path", VALID, ids=lambda p: p.name)
def test_valid_examples_keep_the_rules_no_validator_states(path):
    """Each valid example keeps the linkset rule and the URI pattern rule."""
    record = _load(path)
    if _class(path) == "Linkset":
        assert not linkset_faults(record), linkset_faults(record)
    if _class(path) in ("Dataset", "Linkset"):
        assert not pattern_faults(record), pattern_faults(record)


A = "http://data.example.org/void.ttl#A"
B = "http://data.example.org/void.ttl#B"
C = "http://data.example.org/void.ttl#C"


@pytest.mark.parametrize(
    ("record", "fault"),
    [
        ({"target": [A, A]}, "names 1 distinct datasets"),
        ({"target": [A, A], "subjectsTarget": B}, "repeats a target"),
        (
            {"subjectsTarget": A, "objectsTarget": A},
            "both its subjects' and its objects'",
        ),
        (
            {"target": [A, B], "subjectsTarget": C, "objectsTarget": B},
            "names 3 distinct",
        ),
        (
            {"target": [A, B], "subjectsTarget": A, "objectsTarget": A},
            "both its subjects'",
        ),
    ],
)
def test_the_linkset_rule_finds_what_the_validator_passes(record, fault):
    """Records the validator accepts but VoID's linkset rule refuses."""
    assert not validate(dict(record, id=C), str(SCHEMA), "Linkset").results
    assert any(fault in f for f in linkset_faults(record)), linkset_faults(record)


@pytest.mark.parametrize(
    ("record", "fault"),
    [
        (
            {"uriRegexPattern": "^http://data\\.example\\.org/(lighthouse"},
            "does not compile",
        ),
        (
            {"uriSpace": "http://data.example.org/lighthouse/", "exampleResource": [A]},
            "does not start with the uriSpace",
        ),
        (
            {
                "uriRegexPattern": "^http://data\\.example\\.org/lighthouse/",
                "rootResource": [A],
            },
            "does not match the uriRegexPattern",
        ),
    ],
)
def test_the_pattern_rule_finds_what_the_validator_passes(record, fault):
    """Records the validator accepts but the URI pattern rule refuses."""
    assert not validate(dict(record, id=C), str(SCHEMA), "Dataset").results
    assert any(fault in f for f in pattern_faults(record)), pattern_faults(record)

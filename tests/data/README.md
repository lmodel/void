# Example data for void

This folder holds the examples the tests check, in subfolders:

- `valid` for data that conforms to the schema.
- `invalid` for counter-examples. The first line of each, `# Fails at: <pointer>`, names where the validator must report it.
- `problem/valid` for valid data that the generated dataclasses cannot load under LinkML 1.12.1: a class partition's `class` key is a Python keyword. `tests/test_data.py` validates these examples and loads them through the Pydantic model; the example runner leaves them out.

Each file name is `ClassName-anything.yaml`, and the part before the first `-` names the class the file is checked against.

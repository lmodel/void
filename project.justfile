## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/void.yaml` is the copy `lokf adapt` writes from the schema so that it
# can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The
# roots are the three classes whose instances VoID names by an IRI: a Dataset
# (and so a Linkset, its subclass), a DatasetDescription, the document that
# describes datasets, and a TechnicalFeature. A concept may name any of them
# as its `type`. The partitions stay values inside their dataset. The prefix
# names what the copy renames to keep apart from LOKF (VoidDataset,
# void_title). `--keep source` keeps dcterms:source apart from LOKF's slot of
# the same IRI, whose range is a concept where VoID's is any resource. The
# recipes run the `lokf` the sidecar's floor pins (0.9.0 or later); LOKF_CMD
# runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root Dataset --root DatasetDescription --root TechnicalFeature --prefix void --keep source"

# Rewrite .lokf/void.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/void.yaml

# Fail when .lokf/void.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/void.yaml --check

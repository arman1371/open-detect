# Algorithms

Three algorithms ship with the library. Each is a faithful implementation of a published paper,
and each page below explains the idea, shows a complete example, and documents the knobs.

| Algorithm | Paper | Operating model |
|---|---|---|
| [`raha`](raha.md) | Mahdavi et al., *Raha: A Configuration-Free Error Detection System*, SIGMOD 2019 | Semi-supervised (about 20 labels), single table, pandas-native |
| [`auto_validate`](auto-validate.md) | Song & He, *Auto-Validate: Unsupervised Data Validation Using Data-Domain Patterns Inferred from Data Lakes*, SIGMOD 2021 | Corpus-driven, unsupervised, single table, pandas-native |
| [`uni_detect`](uni-detect.md) | Wang & He, *Uni-Detect: A Unified Approach to Automated Error Detection in Tables*, SIGMOD 2019 | Corpus-driven, unsupervised, Spark and Unity Catalog native |

Not sure which to pick? Start with [Choosing an algorithm](../guides/choosing-an-algorithm.md).

## Fidelity to the papers

The implementations follow the papers closely and document every deviation in module docstrings
and in the [Architecture](../architecture.md) page. Two examples worth knowing:

- Where a paper's formula lost an operator in PDF extraction (the Uni-Detect FD metric, Raha's
  histogram normalization), the implementation uses the standard literature definition that
  reproduces the paper's own worked example.
- Where a paper gives no default (Auto-Validate's horizontal-cut tolerance `theta`), the library
  picks one and says so in the parameter's documentation.

# PRD: API Validation Framework for open-detect

## 1. Summary

This document specifies the API Validation Framework for open-detect, a library of pluggable, paper-backed error detection algorithms for tabular data. The framework provides unified, cross-algorithm input validation for all `detect()` entry points, ensuring consistent error messages, type safety, and parameter checking across all algorithms (Uni-Detect, Raha, Auto-Validate) while remaining extensible for future algorithms.

---

## 2. Contacts

| Name | Role | Comment |
|------|------|---------|
| BackendPM | Product Manager | Owner of API surface and release criteria |
| BackendDev | Backend Engineer | Implementation and test coverage |
| CodeReviewer | Code Reviewer | Review gatekeeper for PRs |

---

## 3. Background

### 3.1 Context

open-detect implements three distinct error detection algorithms from SIGMOD papers:
- **Uni-Detect** (Wang & He, SIGMOD 2019): Corpus-driven, unsupervised, Spark/Unity Catalog-native
- **Raha** (Mahdavi et al., SIGMOD 2019): Semi-supervised (≤20 labels), single-table, pandas-native
- **Auto-Validate** (Song & He, SIGMOD 2021): Corpus-driven, unsupervised, single-table, pandas-native

Each algorithm has fundamentally different operating models and input types, but they all share a common `detect()` contract returning `AlgorithmResult`. The validation framework ensures that callers get consistent, helpful error messages regardless of which algorithm they use.

### 3.2 Why Now?

- **Inconsistent validation**: Historically, each algorithm implemented its own validation logic, leading to inconsistent error messages and behavior
- **Growing algorithm surface**: As more algorithms are added (via the plugin entry-point mechanism), a shared validation layer prevents duplication
- **User experience**: Developers switching between algorithms should not need to learn different error formats
- **Type safety**: Static analysis and runtime validation should align for better IDE support

### 3.3 Recent Changes

- Validation utilities consolidated in `src/open_detect/validation.py` (single source of truth)
- Exception hierarchy formalized in `src/open_detect/exceptions.py` with `ValidationError` as primary validation exception
- All three algorithms now use the shared validation utilities in their `detect()` methods

---

## 4. Objective

### 4.1 Primary Objective

Provide a unified, reusable validation framework that all error detection algorithms in open-detect use for their public `detect()` entry points, ensuring:
- Consistent error messages and exception types across algorithms
- Type-safe parameter validation with clear, actionable error messages
- Extensibility for new algorithms without re-implementing common checks
- Backward compatibility with existing caller code

### 4.2 Business Benefits

- **Reduced support burden**: Consistent errors mean fewer "how do I fix this?" questions
- **Faster onboarding**: New algorithm authors get validation for free
- **Higher reliability**: Centralized validation = fewer validation bugs
- **Better DX**: IDE autocomplete works because types match runtime checks

### 4.3 Key Results (SMART OKRs)

| Objective | Key Result | Target |
|-----------|------------|--------|
| Consistent validation | All 3 algorithms use shared validation utilities | 100% coverage |
| Error message quality | All ValidationError messages follow format: "What went wrong. What was expected. What was received." | 100% compliance |
| Type safety | `mypy --strict` passes on validation module | 0 errors |
| Test coverage | All validation functions have unit tests covering happy path + 3+ error cases each | ≥95% line coverage |
| Extensibility | New algorithm can adopt validation in ≤5 lines of code | Verified by example |

---

## 5. Market Segment(s)

### 5.1 Primary Segment

**Data engineers and ML engineers** building data quality pipelines who:
- Use open-detect as a library in their ETL/ELT workflows
- Switch between algorithms (Uni-Detect for catalog-scale, Raha for ad-hoc, Auto-Validate for pattern-based)
- Need reliable, actionable error messages when they misconfigure a `detect()` call

### 5.2 Secondary Segment

**Algorithm authors** (internal or third-party via entry points) who:
- Implement new `ErrorDetectionAlgorithm` subclasses
- Want validation "for free" without copying boilerplate
- Need the validation framework to be composable and non-opinionated about algorithm-specific parameters

### 5.3 Constraints

- **No mandatory dependencies**: Validation module must work with only `numpy` + `pandas` (core extras)
- **Optional PySpark**: Spark DataFrame checks must be soft (no-op when PySpark unavailable)
- **Performance**: Validation must add <1ms overhead per `detect()` call
- **Python 3.9+**: Must support current minimum version

---

## 6. Value Proposition(s)

### 6.1 Customer Jobs/Needs

| Job | Current Pain | Our Solution |
|-----|--------------|--------------|
| "I passed wrong param to detect()" | Cryptic `TypeError` or silent wrong behavior | Clear `ValidationError: "Unknown parameter 'foo'. Accepted: table_id, columns"` |
| "I passed a string where a list was expected" | Iterates character-by-character silently | `ValidationError: "expected a sequence of str, got str; wrap in a list"` |
| "I passed a pandas DF to Uni-Detect" | Confusing error deep in Spark code | `ValidationError: "data must be a pyspark.sql.DataFrame, got pandas.DataFrame"` |
| "I want to add a new algorithm" | Must reimplement validation from scratch | Import and compose `validation._check_unknown_kwargs()`, etc. |

### 6.2 Gains

- **Predictable errors**: Same error format regardless of algorithm
- **Self-documenting**: Error messages list accepted parameters
- **Fail-fast**: Invalid inputs caught before expensive computation

### 6.3 Pain Avoidance

- No more debugging why `columns="name"` silently fails (should be `columns=["name"]`)
- No more `AttributeError` from passing wrong DataFrame type
- No more silent wrong results from typo'd parameter names

### 6.4 Competitive Advantage

Unlike ad-hoc validation in competitor libraries, our framework:
- Is **shared across algorithms** (not per-algorithm)
- Handles **Sequence[str] vs str** correctly (common footgun)
- Has **soft Spark checks** (works in pandas-only environments)
- Uses **structured exceptions** (`ValidationError` inherits from `ValueError` for backward compat)

---

## 7. Solution

### 7.1 Architecture Overview

```
src/open_detect/
├── validation.py          # Shared validation utilities (this PRD)
├── exceptions.py          # Exception hierarchy (ValidationError, etc.)
├── algorithms/
│   ├── base.py            # ErrorDetectionAlgorithm abstract base
│   ├── auto_validate/
│   │   └── detector.py    # Uses validation._check_unknown_kwargs, _check_columns_present
│   ├── raha/
│   │   └── detector.py    # Uses validation._ensure_dataframe_is_spark, _validate_literal_value
│   └── uni_detect/
│       └── pipeline.py    # Uses validation utilities in _validate_inputs()
```

### 7.2 Key Features

#### 7.2.1 Unknown Kwargs Rejection
```python
# validation.py
def _check_unknown_kwargs(kwargs: dict[str, Any], accepted: set[str], param_name: str = "detect") -> None:
    """Raise ValidationError if kwargs contains keys not in ``accepted``."""
    unknown = set(kwargs) - accepted
    if unknown:
        msg = (
            f"Unknown parameter(s) in {param_name}: {', '.join(sorted(unknown))}. "
            f"Accepted parameters: {', '.join(sorted(accepted))}"
        )
        raise ValidationError(msg)
```

**Usage in algorithms:**
```python
# auto_validate/detector.py
_check_unknown_kwargs(kwargs, {"table_id", "columns", "skip_missing"})

# raha/detector.py (via _reject_unknown_kwargs alias)
_reject_unknown_kwargs(kwargs, {"table_id", "conflict_resolution", "variant", "labeler"})
```

#### 7.2.2 Type Checking with Sequence[str] Special Handling
```python
def _check_expected_type(value: Any, expected_type: type, param_name: str) -> None:
    """Raise ValidationError if value is not of expected type.
    
    For Sequence[str], also rejects bare str (which would be iterated character-by-character).
    """
    origin = get_origin(expected_type)
    if origin is not None and origin is Sequence:
        args = getattr(expected_type, "__args__", ())
        if args and args[0] is str and isinstance(value, str):
            raise ValidationError("expected a sequence of str, got str; wrap in a list")
    if expected_type is not None and not isinstance(value, expected_type):
        raise ValidationError(...)
```

#### 7.2.3 Literal Value Validation
```python
def _validate_literal_value(value: Any, valid_values: set[str], param_name: str) -> None:
    """Validate that value is one of the allowed Literal values.
    
    Checks isinstance(value, str) before set membership to avoid TypeError on unhashable types.
    """
    if not isinstance(value, str):
        raise ValidationError(f"{param_name} must be one of {sorted(valid_values)}, got {value!r}")
    if value not in valid_values:
        raise ValidationError(f"{param_name} must be one of {sorted(valid_values)}, got {value!r}")
```

**Usage:**
```python
# raha/detector.py
_validate_literal_value(conflict_resolution, {"homogeneity", "majority"}, "conflict_resolution")
_validate_literal_value(variant, {"A", "B"}, "variant")
```

#### 7.2.4 Column Uniqueness Check
```python
def _check_columns_unique(columns: list[str]) -> None:
    """Raise ValidationError if column names are not unique strings."""
    if not all(isinstance(c, str) for c in columns):
        raise ValidationError("All column names must be strings, got non-string entries")
    if len(columns) != len(set(columns)):
        duplicates = [c for c in columns if columns.count(c) > 1]
        raise ValidationError(f"Column names must be unique, got duplicates: {', '.join(sorted(set(duplicates)))}")
```

#### 7.2.5 DataFrame Type Validation (Spark + pandas)

**Strict check (Uni-Detect):**
```python
def _check_dataframe_is_spark(df: Any, param_name: str = "data") -> None:
    """Validate that data is a Spark DataFrame. Raises if PySpark unavailable."""
    try:
        from pyspark.sql import DataFrame as SparkDataFrame
        if not isinstance(df, SparkDataFrame):
            raise ValidationError(...)
    except ImportError:
        raise ValidationError("PySpark is required for this algorithm but not installed")
```

**Soft check (Raha/Auto-Validate):**
```python
def _ensure_dataframe_is_spark(df: Any, param_name: str = "data") -> None:
    """Runtime guard: accepts Spark OR pandas DataFrames. Never rejects non-DataFrame input."""
    try:
        from pyspark.sql import DataFrame as SparkDataFrame
        if isinstance(df, SparkDataFrame):
            return
    except ImportError:
        pass
    try:
        import pandas as pd
    except ImportError:
        return
    if isinstance(df, pd.DataFrame):
        return
    # Falls through silently - caller handles non-DataFrame case
```

#### 7.2.6 Sequence of Strings Validation
```python
def _ensure_sequence_of_str(value: Any, param_name: str) -> None:
    """Raise ValidationError if value is not a sequence of strings.
    
    Also rejects bare str (which would be iterated character-by-character).
    """
    if isinstance(value, str):
        raise ValidationError(f"{param_name} must be a sequence of str, got str; wrap in a list")
    if not isinstance(value, Sequence):
        raise ValidationError(f"{param_name} must be a sequence of str, got {type(value).__name__}")
    for i, item in enumerate(value):
        if not isinstance(item, str):
            raise ValidationError(f"{param_name}[{i}] must be str, got {type(item).__name__}")
```

#### 7.2.7 Column Presence Check (Algorithm-specific)
```python
# auto_validate/detector.py (local to algorithm)
def _check_columns_present(
    columns: list[str] | None, df_columns: list[str], skip_missing: bool = False
) -> None:
    if columns is None:
        return
    missing = [c for c in columns if c not in df_columns]
    if missing and not skip_missing:
        raise ValidationError(f"Requested column(s) not found in DataFrame: {', '.join(missing)}")
```

### 7.3 Technology

- **Language**: Python 3.9+
- **Type system**: Uses `typing.get_origin`, `typing.get_args` for runtime generic inspection
- **Dependencies**: Zero additional deps (uses only stdlib `collections.abc`, `typing`)
- **Testing**: pytest with parametrized tests for all validation functions

### 7.4 Assumptions

| Assumption | Validation |
|------------|------------|
| Callers use keyword arguments for `detect()` | `detect()` signatures use `*,` to enforce keyword-only params |
| PySpark may not be installed | Soft checks in `_ensure_dataframe_is_spark` |
| Algorithms may have unique parameters | `_check_unknown_kwargs` accepts algorithm-specific `accepted` set |
| Error messages must be actionable | All messages include: what went wrong, expected, received |
| Performance matters | Validation is O(n) in parameter count, no I/O |

---

## 8. Release

### 8.1 Timeline

| Phase | Scope | Target |
|-------|-------|--------|
| **Phase 1 (Current)** | Core validation utilities + 3 algorithm integrations | Complete |
| **Phase 2** | Documentation + examples in README | 2 weeks |
| **Phase 3** | Third-party algorithm author guide | 4 weeks |

### 8.2 Versioning

- Validation framework is part of `open-detect` core (no extra required)
- `ValidationError` is public API (re-exported from `open_detect.exceptions`)
- Breaking changes to validation utilities require minor version bump

### 8.3 Migration Path

For existing callers:
- No migration needed - validation only adds stricter checks, never loosens
- New errors are `ValidationError` (subclass of `ValueError`) so existing `except ValueError` handlers still work
- Algorithm-specific parameter validation is additive

### 8.4 Future Extensions (Post-MVP)

| Feature | Description | Priority |
|---------|-------------|----------|
| Parameter deprecation warnings | Warn when caller uses deprecated param name | Medium |
| JSON Schema export | Generate OpenAPI/JSON Schema for `detect()` params | Low |
| Pydantic integration | Optional Pydantic model for `detect()` input validation | Low |
| Async validation | For future async `detect()` variants | Low |

---

## Appendix: Validation Function Reference

| Function | Purpose | Used By |
|----------|---------|---------|
| `_check_unknown_kwargs` | Reject unknown keyword arguments | All algorithms |
| `_reject_unknown_kwargs` | Alias with different message format | Raha |
| `_check_expected_type` | Generic type check with Sequence[str] handling | Auto-Validate (internal) |
| `_validate_literal_value` | Check value against allowed Literal set | Raha, Uni-Detect |
| `_check_columns_unique` | Ensure column names are unique strings | Auto-Validate (internal) |
| `_check_dataframe_is_spark` | Strict Spark DataFrame check | Uni-Detect |
| `_ensure_dataframe_is_spark` | Soft Spark/pandas DataFrame check | Raha, Auto-Validate |
| `_ensure_sequence_of_str` | Validate sequence of strings | Uni-Detect |
| `_check_columns_present` | Verify requested columns exist in DataFrame | Auto-Validate (algorithm-local) |

---

## Appendix: Exception Hierarchy

```
OpenDetectError (base)
├── ValidationError (ValueError)     # Bad caller input
├── ConfigurationError               # Invalid config object
├── UnknownAlgorithmError            # Algorithm not registered
└── IndexNotBuiltError               # Auto-Validate index missing
```

All validation functions raise `ValidationError` with messages following the pattern:
> "{what went wrong}. {what was expected}. {what was received}."

Example:
> "Unknown parameter(s) in detect: foo. Accepted parameters: table_id, columns, skip_missing. Got: foo=123"
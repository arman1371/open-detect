"""Tests for the deprecated import shims. Delete this module in 0.5.0 with the shims."""

from __future__ import annotations

import importlib
import subprocess
import sys
import warnings

import pytest

from open_detect.algorithms.uni_detect import exceptions as new_exc
from open_detect.algorithms.uni_detect import text_utils as new_text
from open_detect.algorithms.uni_detect.core import enums as new_enums
from open_detect.algorithms.uni_detect.core import models as new_models

NEW = "open_detect.algorithms.uni_detect"


def _fresh_import(name: str):
    sys.modules.pop(name, None)
    with pytest.warns(DeprecationWarning, match=NEW) as rec:
        mod = importlib.import_module(name)
    assert len([w for w in rec if issubclass(w.category, DeprecationWarning)]) == 1
    return mod


@pytest.mark.parametrize(
    ("old", "new", "names"),
    [
        (
            "open_detect.core.enums",
            new_enums,
            ["ErrorType", "ColumnDataType", "ComparisonDirection"],
        ),
        (
            "open_detect.core.models",
            new_models,
            [
                "Candidate",
                "Detection",
                "FeatureBucket",
                "MetricObservation",
                "CorpusColumnRecord",
                "CorpusPairRecord",
            ],
        ),
        (
            "open_detect.text_utils",
            new_text,
            [
                "tokenize",
                "is_integer_like",
                "is_float_like",
                "is_mixed_alphanumeric",
                "infer_column_data_type",
            ],
        ),
    ],
)
def test_module_shims_are_identity_preserving(old, new, names):
    mod = _fresh_import(old)
    for n in names:
        assert getattr(mod, n) is getattr(new, n)


@pytest.mark.parametrize(
    "name",
    ["CorpusNotFoundError", "UnityCatalogError", "InsufficientDataError", "DataQualityError"],
)
def test_exceptions_getattr_shim(name):
    import open_detect.exceptions as old

    with pytest.warns(DeprecationWarning, match=NEW):
        cls = getattr(old, name)
    assert cls is getattr(new_exc, name)


def test_old_except_clause_catches_new_error():
    import open_detect.exceptions as old

    with warnings.catch_warnings():
        warnings.simplefilter("ignore", DeprecationWarning)
        caught = old.CorpusNotFoundError
    with pytest.raises(caught):
        raise new_exc.CorpusNotFoundError("x")


def test_unknown_exception_attr_raises():
    import open_detect.exceptions as old

    with pytest.raises(AttributeError):
        old.NoSuchError  # noqa: B018


def test_core_package_getattr_shim():
    import open_detect.core as old

    with pytest.warns(DeprecationWarning, match=NEW):
        assert old.ErrorType is new_enums.ErrorType


def test_internal_imports_use_new_paths_only():
    code = (
        "import importlib, pkgutil, open_detect\n"
        "for m in pkgutil.walk_packages(open_detect.__path__, 'open_detect.'):\n"
        "    if m.name in DEPRECATED or m.name.startswith('open_detect.core'):\n"
        "        continue\n"
        "    try:\n"
        "        importlib.import_module(m.name)\n"
        "    except ImportError as e:\n"
        "        if 'pyspark' not in str(e) and 'delta' not in str(e):\n"
        "            raise\n"
    )
    code = "DEPRECATED = {'open_detect.text_utils', 'open_detect.exceptions'}\n" + code
    subprocess.run([sys.executable, "-W", "error::DeprecationWarning", "-c", code], check=True)


def test_from_core_import_submodule():
    import open_detect.core as old

    sys.modules.pop("open_detect.core.enums", None)
    old.__dict__.pop("enums", None)
    with pytest.warns(DeprecationWarning, match=NEW):
        from open_detect.core import enums  # noqa: F401


def test_core_missing_attr_raises():
    import open_detect.core as old

    with pytest.raises(AttributeError):
        old.NoSuchThing  # noqa: B018

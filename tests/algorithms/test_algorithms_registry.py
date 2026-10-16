"""Unit tests for the open_detect.algorithms registry and base contract."""

from __future__ import annotations

from pathlib import Path

import pytest

from open_detect.algorithms import list_algorithms, registry
from open_detect.algorithms.base import AlgorithmResult, CellResult
from open_detect.algorithms.registry import (
    UnknownAlgorithmError,
    get_algorithm,
    get_algorithm_class,
    register_lazy,
)


def test_builtin_algorithms_are_registered():
    assert {"auto_validate", "raha", "uni_detect"} <= set(list_algorithms())


def test_unknown_algorithm_raises():
    with pytest.raises(UnknownAlgorithmError, match="unknown"):
        get_algorithm_class("unknown")


def test_get_algorithm_constructs_with_args():
    from open_detect.algorithms.raha import RahaConfig, RahaDetector

    config = RahaConfig(labeling_budget=5)
    algo = get_algorithm("raha", config)
    assert isinstance(algo, RahaDetector)
    assert algo.config.labeling_budget == 5


def test_register_lazy_overrides_existing_name():
    class Dummy:
        name = "dummy"

    register_lazy("dummy", lambda: Dummy)
    try:
        assert get_algorithm_class("dummy") is Dummy
        assert "dummy" in list_algorithms()
    finally:
        registry._registry.pop("dummy", None)


def test_register_lazy_is_lazy():
    calls = []

    def factory():
        calls.append(1)
        return object

    register_lazy("lazy_probe", factory)
    try:
        assert calls == []  # registering must not import/construct anything
        get_algorithm_class("lazy_probe")
        assert calls == [1]
    finally:
        registry._registry.pop("lazy_probe", None)


class TestAlgorithmResult:
    def test_errors_filters_to_flagged_cells(self):
        result = AlgorithmResult(
            algorithm="test",
            cells=(
                CellResult("t", 0, "a", "test", True, 0.9),
                CellResult("t", 1, "a", "test", False, 0.1),
            ),
        )
        assert result.errors() == (result.cells[0],)
        assert len(result) == 2

    def test_to_pandas_has_shared_schema(self):
        result = AlgorithmResult(
            algorithm="test", cells=(CellResult("t", 0, "a", "test", True, 0.9, {"x": 1}),)
        )
        frame = result.to_pandas()
        assert frame.loc[0, "is_error"]
        assert frame.loc[0, "evidence"] == {"x": 1}

    def test_union_combines_multiple_results(self):
        a = AlgorithmResult("a", (CellResult("t", 0, "a", "a", True, 1.0),))
        b = AlgorithmResult("b", (CellResult("t", 1, "b", "b", False, 0.0),))
        combined = AlgorithmResult.union([a, b])
        assert len(combined) == 2
        assert combined.algorithm == "ensemble"


class TestCellResultEvidence:
    def test_evidence_is_copied_on_construction(self):
        shared = {"k": [1, 2]}
        a = CellResult("t", 0, "a", "x", True, 1.0, shared)
        b = CellResult("t", 1, "a", "x", True, 1.0, shared)
        shared["k"].append(3)
        shared["new"] = 1
        assert a.evidence == {"k": [1, 2]}
        assert b.evidence == {"k": [1, 2]}
        assert a.evidence is not b.evidence

    def test_evidence_is_read_only(self):
        cell = CellResult("t", 0, "a", "x", True, 1.0, {"k": 1})
        with pytest.raises(TypeError):
            cell.evidence["k"] = 2  # type: ignore[index]
        with pytest.raises(TypeError):
            del cell.evidence["k"]  # type: ignore[attr-defined]

    def test_to_dict_returns_independent_json_serialisable_copy(self):
        import json

        cell = CellResult("t", 0, "a", "x", True, 1.0, {"k": [1]})
        d = cell.to_dict()
        assert json.loads(json.dumps(d))["evidence"] == {"k": [1]}
        d["evidence"]["k"].append(2)
        assert cell.evidence == {"k": [1]}

    def test_equality_and_pickle_roundtrip(self):
        import copy
        import pickle

        cell = CellResult("t", 0, "a", "x", True, 1.0, {"k": 1})
        assert cell == CellResult("t", 0, "a", "x", True, 1.0, {"k": 1})
        assert pickle.loads(pickle.dumps(cell)) == cell
        assert copy.deepcopy(cell) == cell

    def test_default_evidence_is_empty(self):
        assert CellResult("t", 0, "a", "x", True, 1.0).evidence == {}


class _FakeEntryPoint:
    def __init__(self, name, loader):
        self.name = name
        self.value = f"fake_pkg:{name}"
        self._loader = loader
        self.load_calls = 0

    def load(self):
        self.load_calls += 1
        return self._loader()


@pytest.fixture
def fresh_registry(monkeypatch):
    """Isolated registry state with controllable fake entry points."""
    monkeypatch.setattr(registry, "_registry", {})
    monkeypatch.setattr(registry, "_entry_points_loaded", False)

    def install(*eps):
        monkeypatch.setattr(registry.metadata, "entry_points", lambda group: list(eps))

    return install


def _good_plugin_class():
    from open_detect.algorithms.base import ErrorDetectionAlgorithm

    class Good(ErrorDetectionAlgorithm):
        name = "good"

        def detect(self, data, *, table_id="table", **kwargs):
            return AlgorithmResult("good", ())

    return Good


def _write_distinfo_plugin(
    tmp_path: Path,
    *,
    group: str = "open_detect.algorithms",
    plugin_name: str = "distinfo_plugin",
) -> Path:
    """Write a real ``<pkg>.dist-info`` tree onto ``tmp_path``.

    This mirrors what an installed third-party wheel contributes: a package
    module plus a ``*.dist-info/entry_points.txt`` declaring the algorithm
    under the ``open_detect.algorithms`` group. Placing the directory on
    ``sys.path`` lets :func:`registry._load_entry_points` be exercised
    through the real ``importlib.metadata`` code path (the one used in
    production) instead of the monkeypatched ``_FakeEntryPoint`` path used by
    the rest of this file.
    """
    pkg_dir = tmp_path / "distinfo_plugin_pkg"
    pkg_dir.mkdir(exist_ok=True)
    (pkg_dir / "__init__.py").write_text(
        "from open_detect.algorithms.base import ErrorDetectionAlgorithm, AlgorithmResult\n"
        "\n"
        "class DistInfoPlugin(ErrorDetectionAlgorithm):\n"
        "    name = 'distinfo_plugin'\n"
        "    def detect(self, data, *, table_id='table', **kwargs):\n"
        "        return AlgorithmResult('distinfo_plugin', ())\n"
    )
    dist_info = tmp_path / "distinfo_plugin_pkg-1.0.0.dist-info"
    dist_info.mkdir(exist_ok=True)
    (dist_info / "METADATA").write_text(
        "Metadata-Version: 2.1\nName: distinfo-plugin-pkg\nVersion: 1.0.0\n"
    )
    (dist_info / "entry_points.txt").write_text(
        f"[{group}]\n{plugin_name} = distinfo_plugin_pkg:DistInfoPlugin\n"
    )
    return tmp_path


@pytest.fixture
def real_plugin_path(tmp_path, monkeypatch):
    """A real dist-info plugin directory prepended to ``sys.path``."""
    path = _write_distinfo_plugin(tmp_path)
    monkeypatch.syspath_prepend(str(path))
    # Reset registry state so discovery re-reads importlib.metadata from scratch.
    monkeypatch.setattr(registry, "_registry", {})
    monkeypatch.setattr(registry, "_entry_points_loaded", False)
    yield path


class TestPluginDiscovery:
    def test_valid_plugin_is_registered(self, fresh_registry):
        good = _good_plugin_class()
        fresh_registry(_FakeEntryPoint("good", lambda: good))
        assert "good" in list_algorithms()
        assert get_algorithm_class("good") is good

    def test_load_failure_is_logged_and_skipped(self, fresh_registry, caplog):
        def boom():
            raise ImportError("missing dependency")

        good = _good_plugin_class()
        fresh_registry(_FakeEntryPoint("broken", boom), _FakeEntryPoint("good", lambda: good))
        with caplog.at_level("WARNING", logger="open_detect"):
            names = list_algorithms()
        assert names == ["good"]
        warning = next(r for r in caplog.records if r.levelname == "WARNING")
        assert "broken" in warning.getMessage()
        assert warning.exc_info is not None
        with pytest.raises(UnknownAlgorithmError):
            get_algorithm_class("broken")

    def test_non_subclass_is_rejected_with_log(self, fresh_registry, caplog):
        class NotAnAlgorithm:
            pass

        fresh_registry(
            _FakeEntryPoint("bad_class", lambda: NotAnAlgorithm),
            _FakeEntryPoint("bad_obj", lambda: "just a string"),
        )
        with caplog.at_level("WARNING", logger="open_detect"):
            assert list_algorithms() == []
        messages = " ".join(r.getMessage() for r in caplog.records)
        assert "bad_class" in messages and "bad_obj" in messages
        assert "ErrorDetectionAlgorithm" in messages

    def test_plugin_cannot_shadow_builtin_and_builtins_skip_discovery(self, fresh_registry):
        good = _good_plugin_class()
        ep = _FakeEntryPoint("raha", lambda: good)
        fresh_registry(ep)
        register_lazy("raha", lambda: object)  # stand-in built-in
        assert get_algorithm_class("raha") is object
        assert ep.load_calls == 0  # resolving a registered name never imports plugins
        assert "raha" in list_algorithms()
        assert get_algorithm_class("raha") is object
        assert ep.load_calls == 0

    def test_concurrent_first_lookups_discover_once(self, fresh_registry):
        import threading
        import time

        good = _good_plugin_class()

        def slow_loader():
            time.sleep(0.05)
            return good

        ep = _FakeEntryPoint("good", slow_loader)
        fresh_registry(ep)
        results: list[object] = []
        errors: list[BaseException] = []

        def worker():
            try:
                results.append(get_algorithm_class("good"))
            except BaseException as exc:  # pragma: no cover - failure path
                errors.append(exc)

        threads = [threading.Thread(target=worker) for _ in range(8)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        assert errors == []
        assert results == [good] * 8
        assert ep.load_calls == 1


class TestPluginDiscoveryViaRealDistInfo:
    """Discovery through a real ``*.dist-info`` directory on ``sys.path``.

    These tests exercise ``registry._load_entry_points`` via the production
    ``importlib.metadata`` path (a real ``entry_points.txt`` file), as opposed
    to the ``_FakeEntryPoint`` monkeypatch used by ``TestPluginDiscovery``.
    They are the only tests that fail when the entry-point group name is
    changed, so they pin the contract that third-party wheels rely on.
    """

    def test_distinfo_plugin_is_discovered(self, real_plugin_path):
        assert "distinfo_plugin" in list_algorithms()

    def test_distinfo_plugin_resolves_to_real_class(self, real_plugin_path):
        from distinfo_plugin_pkg import DistInfoPlugin

        assert get_algorithm_class("distinfo_plugin") is DistInfoPlugin

    def test_distinfo_plugin_constructs(self, real_plugin_path):
        from distinfo_plugin_pkg import DistInfoPlugin

        algo = get_algorithm("distinfo_plugin")
        assert isinstance(algo, DistInfoPlugin)
        assert algo.name == "distinfo_plugin"

    def test_group_name_change_breaks_discovery(self, real_plugin_path, monkeypatch):
        """A renamed group means the plugin is invisible: discovery is empty."""
        # Re-write the entry_points.txt under a different group name and reset
        # the registry so discovery re-reads importlib.metadata from scratch.
        entry_points_txt = real_plugin_path / "distinfo_plugin_pkg-1.0.0.dist-info" / "entry_points.txt"
        entry_points_txt.write_text(
            "[other.group]\ndistinfo_plugin = distinfo_plugin_pkg:DistInfoPlugin\n"
        )
        monkeypatch.setattr(registry, "_registry", {})
        monkeypatch.setattr(registry, "_entry_points_loaded", False)

        assert "distinfo_plugin" not in list_algorithms()
        with pytest.raises(UnknownAlgorithmError):
            get_algorithm_class("distinfo_plugin")

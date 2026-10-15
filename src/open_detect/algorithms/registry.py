"""Registry mapping algorithm names to :class:`~open_detect.algorithms.base.ErrorDetectionAlgorithm` classes.

Two registration paths feed the same registry:

1. **Built-in algorithms** (``uni_detect``, ``raha``) register themselves via
   :func:`register_lazy` when :mod:`open_detect.algorithms` is imported. The
   factory is a zero-argument callable rather than the class itself so that
   importing :mod:`open_detect.algorithms` never pulls in an algorithm's heavy,
   optional dependencies (``pyspark`` for Uni-Detect, ``scikit-learn`` for
   Raha) -- those are only imported the first time that specific algorithm is
   requested, mirroring the lazy-import trick already used in
   ``open_detect/__init__.py``.
2. **Third-party algorithms** are discovered via the ``open_detect.algorithms``
   Python entry-point group (see ``pyproject.toml``). Any installed package
   that declares ``my_algo = "my_package.module:MyAlgorithmClass"`` under that
   group becomes available through :func:`get_algorithm` /
   :func:`list_algorithms` with no code changes here -- this is the extension
   point for "add more algorithms later" without editing this library.

   Plugins are loaded eagerly during discovery so a broken or non-conforming
   plugin is logged at WARNING and skipped rather than crashing a later
   lookup. Discovery only runs when a name is not already registered (or when
   listing), so resolving a built-in never imports third-party code.

All registry mutation and the discovery once-flag are guarded by a re-entrant
lock, so concurrent first lookups from several threads are safe.
"""

from __future__ import annotations

import threading
from collections.abc import Callable
from importlib import metadata
from typing import TYPE_CHECKING

from open_detect.exceptions import OpenDetectError
from open_detect.logging_utils import get_logger

if TYPE_CHECKING:
    from open_detect.algorithms.base import ErrorDetectionAlgorithm

logger = get_logger(__name__)

_ENTRY_POINT_GROUP = "open_detect.algorithms"

_registry: dict[str, Callable[[], type[ErrorDetectionAlgorithm]]] = {}
_entry_points_loaded = False
# Re-entrant: a plugin imported during discovery may itself call register_algorithm().
_lock = threading.RLock()


class UnknownAlgorithmError(OpenDetectError):
    """Raised when :func:`get_algorithm_class` is asked for an unregistered name."""


def register_lazy(name: str, factory: Callable[[], type[ErrorDetectionAlgorithm]]) -> None:
    """Register ``name`` against a zero-argument class factory.

    Re-registering an existing name overwrites it -- useful for tests and for
    a downstream project intentionally swapping out a built-in algorithm.
    """
    with _lock:
        _registry[name] = factory


def register_algorithm(
    name: str,
) -> Callable[[type[ErrorDetectionAlgorithm]], type[ErrorDetectionAlgorithm]]:
    """Class decorator that eagerly registers ``cls`` under ``name``.

    Use this for algorithms whose module has no optional/heavy dependencies
    to hide behind laziness; prefer :func:`register_lazy` otherwise.
    """

    def decorator(cls: type[ErrorDetectionAlgorithm]) -> type[ErrorDetectionAlgorithm]:
        register_lazy(name, lambda: cls)
        return cls

    return decorator


def _constant_factory(
    cls: type[ErrorDetectionAlgorithm],
) -> Callable[[], type[ErrorDetectionAlgorithm]]:
    return lambda: cls


def _load_entry_points() -> None:
    global _entry_points_loaded
    from open_detect.algorithms.base import ErrorDetectionAlgorithm

    with _lock:
        if _entry_points_loaded:
            return
        _entry_points_loaded = True
        try:
            eps = metadata.entry_points(group=_ENTRY_POINT_GROUP)
        except Exception:  # pragma: no cover - defensive against malformed metadata
            logger.warning("Could not read %r entry points", _ENTRY_POINT_GROUP, exc_info=True)
            return
        for ep in eps:
            if ep.name in _registry:
                continue  # a built-in (or an earlier plugin) already claimed this name
            try:
                cls = ep.load()
            except Exception:
                logger.warning(
                    "Skipping algorithm plugin %r (%s): failed to load",
                    ep.name,
                    ep.value,
                    exc_info=True,
                )
                continue
            if not (isinstance(cls, type) and issubclass(cls, ErrorDetectionAlgorithm)):
                logger.warning(
                    "Skipping algorithm plugin %r (%s): %r is not a subclass of "
                    "ErrorDetectionAlgorithm",
                    ep.name,
                    ep.value,
                    cls,
                )
                continue
            register_lazy(ep.name, _constant_factory(cls))


def get_algorithm_class(name: str) -> type[ErrorDetectionAlgorithm]:
    """Resolve ``name`` to its algorithm class, importing it on first use."""
    with _lock:
        if name not in _registry:
            _load_entry_points()
        try:
            factory = _registry[name]
        except KeyError:
            available = ", ".join(sorted(_registry)) or "<none registered>"
            raise UnknownAlgorithmError(
                f"Unknown error-detection algorithm {name!r}. Available: {available}"
            ) from None
    return factory()


def get_algorithm(name: str, *args: object, **kwargs: object) -> ErrorDetectionAlgorithm:
    """Resolve ``name`` and construct it with ``*args, **kwargs``."""
    return get_algorithm_class(name)(*args, **kwargs)


def list_algorithms() -> list[str]:
    """Every registered algorithm name (built-in and plugin-discovered)."""
    _load_entry_points()
    with _lock:
        return sorted(_registry)

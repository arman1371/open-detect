"""Structured logging helpers.

Uses the standard :mod:`logging` module so behavior composes correctly with
Databricks cluster logs (log4j capture) and driver stdout. We deliberately
avoid configuring handlers here -- library code should never call
``logging.basicConfig`` -- and instead let the host application (a notebook,
a Databricks Job, or a test harness) own log configuration.

The one exception is :func:`configure_logging`, which job ``main()`` entry
points (and only those) call to make their INFO output visible.
"""

from __future__ import annotations

import logging
import time
from collections.abc import Iterator
from contextlib import contextmanager

_ROOT_LOGGER_NAME = "open_detect"
LOG_FORMAT = "%(asctime)s %(levelname)s %(name)s: %(message)s"


def configure_logging(level: int = logging.INFO) -> None:
    """Install a root handler via :func:`logging.basicConfig`; call from job ``main()`` only."""
    logging.basicConfig(level=level, format=LOG_FORMAT)


def get_logger(name: str) -> logging.Logger:
    """Return a namespaced logger under the ``open_detect`` hierarchy.

    Parameters
    ----------
    name:
        Typically ``__name__`` of the calling module.
    """
    if name == _ROOT_LOGGER_NAME or name.startswith(f"{_ROOT_LOGGER_NAME}."):
        return logging.getLogger(name)
    return logging.getLogger(f"{_ROOT_LOGGER_NAME}.{name}")


@contextmanager
def log_duration(logger: logging.Logger, action: str, level: int = logging.INFO) -> Iterator[None]:
    """Log the wall-clock duration of a block, tagged with ``action``.

    Example
    -------
    >>> with log_duration(logger, "build_corpus_statistics"):
    ...     builder.run()
    """
    start = time.monotonic()
    logger.log(level, "%s: started", action)
    try:
        yield
    except Exception:
        elapsed = time.monotonic() - start
        logger.exception("%s: failed after %.2fs", action, elapsed)
        raise
    else:
        elapsed = time.monotonic() - start
        logger.log(level, "%s: completed in %.2fs", action, elapsed)

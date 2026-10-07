"""Generalization hierarchy and tokenizer (paper Section 2.1, Figure 4).

Values are tokenized into maximal runs of alphanumeric characters and runs of
symbols; each token is then classified as ``digit`` (all digits), ``letter``
(all letters), ``alphanum`` (a mix of the two) or ``symbol``. A pattern is a
concatenation of literal tokens and bracketed token classes such as
``<digit>{2}``, ``<letter>+`` or ``<num>``.

The node set below reconstructs Figure 4, which exists in the paper only as a
raster image (``figures/hierarchy.png``); see the module's fidelity note in
``ARCHITECTURE.md``. Leaf nodes are the 26 English letters plus ``<symbol>``
for everything else, matching the paper's "leaf-nodes represent the English
alphabet".
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from functools import lru_cache

#: Character classes a token can belong to.
CHAR_CLASSES: tuple[str, ...] = ("digit", "letter", "alphanum", "symbol")

#: Root of the hierarchy. Excluded from every ``P(v)`` because it is trivially
#: consistent with every column (paper Section 2.1).
ROOT_PATTERN = ".*"

#: How general each character class is. Lower means more general, so
#: ``num`` (any number, incl. floats) generalizes further than ``digit``,
#: which in turn generalizes further than ``letter``/``symbol``.
_CLASS_GENERALITY: dict[str, int] = {
    "alphanum": 1,
    "num": 2,
    "digit": 3,
    "letter": 4,
    "symbol": 5,
}

#: Extra generality granted by a ``+`` (any number of characters) over a
#: fixed-width node.
_PLUS_PENALTY: int = 6

_BRACKET_RE = re.compile(r"<(num|digit|letter|alphanum|symbol)>(\{(\d+)\}|\+)?")


@dataclass(frozen=True, slots=True)
class Token:
    """A maximal run of same-class characters, plus its class."""

    text: str
    char_class: str

    @property
    def length(self) -> int:
        return len(self.text)

    def generalizations(self) -> tuple[str, ...]:
        """Every node of the hierarchy this token can be replaced by, coarsest first.

        ``char_class``-bare forms (``<digit>``) mean exactly one character and
        are what the paper writes as ``<digit>{1}``; ``{k}`` means exactly
        ``k`` characters and ``+`` means one or more. ``<num>`` and ``<num>+``
        are retained as distinct spellings of the same language (the paper
        lists both in ``P("9:07")``) so that patterns round-trip to the paper's
        own notation.
        """
        n = self.length
        cls = self.char_class
        coarse: list[str] = []
        fine: list[str] = []
        if cls in ("digit", "letter", "alphanum"):
            coarse.append("<alphanum>+")
            fine.append("<alphanum>" if n == 1 else f"<alphanum>{{{n}}}")
        if cls == "digit":
            coarse.append("<num>")
        if cls in ("digit", "letter"):
            coarse.append(f"<{cls}>+")
            fine.append(f"<{cls}>" if n == 1 else f"<{cls}>{{{n}}}")
        if cls == "symbol":
            coarse.append("<symbol>+")
            fine.append("<symbol>" if n == 1 else f"<symbol>{{{n}}}")
        return (self.text, *coarse, *fine)


def _char_class(ch: str) -> str:
    if ch.isdigit():
        return "digit"
    if ch.isalpha():
        return "letter"
    return "symbol"


def tokenize(value: str) -> tuple[Token, ...]:
    """Split ``value`` into its tokens, per the paper's definition of ``t(v)``.

    "The number of tokens in ``v`` is defined as the number of consecutive
    sequences of letters, digits, or symbols in ``v``" (paper Section 2.4). We
    read that as maximal runs of *alphanumeric* characters (classified by
    whether the run is all digits, all letters, or a mix) and maximal runs of
    non-alphanumeric characters. This keeps ``"2015"`` a single ``<num>`` token,
    which is what the paper's own coarse pattern
    ``<num>/<num>/<num> <num>:<num>:<num> <letter>+`` requires.
    """
    tokens: list[Token] = []
    for run, is_alnum in _iter_runs(value):
        if is_alnum:
            classes = {_char_class(ch) for ch in run}
            cls = classes.pop() if len(classes) == 1 else "alphanum"
        else:
            cls = "symbol"
        tokens.append(Token(run, cls))
    return tuple(tokens)


def _iter_runs(value: str):
    """Yield ``(run, is_alphanumeric)`` for each maximal run in ``value``."""
    if not value:
        return
    start = 0
    run_alnum = value[0].isalnum()
    for i in range(1, len(value) + 1):
        at_end = i == len(value)
        if at_end or value[i].isalnum() != run_alnum:
            yield value[start:i], run_alnum
            if not at_end:
                start = i
                run_alnum = value[i].isalnum()


def token_count(value: str) -> int:
    """``t(v)`` -- the number of tokens in ``value`` (paper Section 2.4)."""
    return len(tokenize(value))


def generalize(tokens: tuple[Token, ...]) -> str:
    """The coarsest pattern in ``P(v)``.

    Alphanumeric tokens generalize to their class's coarsest node (``<num>``
    for digit runs, ``<letter>+``/``<alphanum>+`` otherwise), which reproduces
    the paper's own coarse output for a date-time column --
    ``<num>/<num>/<num> <num>:<num>:<num> <letter>+`` (Section 2.1). Symbol
    tokens keep their literal text: separators like ``/`` and ``:`` are
    structural in that example, and the paper never generalizes them.
    """
    parts: list[str] = []
    for token in tokens:
        if token.char_class == "digit":
            parts.append("<num>")
        elif token.char_class == "symbol":
            parts.append(token.text)
        else:
            parts.append(f"<{token.char_class}>+")
    return "".join(parts)


def generality_weight(pattern: str) -> int:
    """Total generality of ``pattern``; lower means more general.

    Used only to order enumeration (Algorithm 1 emits coarse patterns first
    and drills down into finer ones) and to break ties between equally general
    patterns. It never ranks FMDV candidates -- those are ordered by FPR.
    """
    total = 0
    for match in _BRACKET_RE.finditer(pattern):
        cls = match.group(1)
        suffix = match.group(2)
        total += _CLASS_GENERALITY[cls]
        if suffix == "+":
            total += _PLUS_PENALTY
        elif suffix is not None:
            total += min(int(match.group(3)), 9)
    return total


def _class_of_token(text: str) -> str | None:
    """The character class a literal token belongs to, or ``None`` if mixed."""
    classes = {_char_class(ch) for ch in text}
    return classes.pop() if len(classes) == 1 else None


@lru_cache(maxsize=4096)
def _parse(pattern: str) -> tuple[tuple[str, str, int | None], ...]:
    """Compile a pattern string into ``(kind, class, count)`` parts.

    ``kind`` is ``"literal"`` (with ``class`` holding one token's text and
    ``count`` ``None``) or ``"class"`` (with ``count`` the exact repetition
    count, or ``None`` for a ``+`` "one or more" form). The bare class name
    without a repetition suffix means exactly one character.

    Literal runs are re-tokenized, so a pattern written the way the paper
    writes one -- the whole value, as in ``P("9:07")``'s ``"9:07"`` -- splits
    into the same per-token parts a bracketed pattern would.
    """
    parts: list[tuple[str, str, int | None]] = []
    pos = 0
    for match in _BRACKET_RE.finditer(pattern):
        _append_literal(parts, pattern[pos : match.start()])
        suffix = match.group(2)
        if suffix is None:
            count: int | None = 1
        elif suffix == "+":
            count = None
        else:
            count = int(match.group(3))
        parts.append(("class", match.group(1), count))
        pos = match.end()
    _append_literal(parts, pattern[pos:])
    return tuple(parts)


def _append_literal(parts: list[tuple[str, str, int | None]], run: str) -> None:
    for token in tokenize(run):
        parts.append(("literal", token.text, None))


def _is_numeric(text: str) -> bool:
    return bool(text) and all(ch.isdigit() for ch in text)


def _part_matches(cls: str, count: int | None, text: str) -> bool:
    if cls in ("num", "digit"):
        ok = _is_numeric(text)
    elif cls == "alphanum":
        ok = text.isalnum()
    elif cls == "letter":
        ok = text.isalpha()
    elif cls == "symbol":
        ok = bool(text) and not text.isalnum()
    else:  # pragma: no cover - the regex cannot produce anything else
        ok = False
    if not ok:
        return False
    if cls == "num":
        return True  # a number stands for a whole numeric run, whatever its length
    if count is None:
        return True  # "+" means one or more, and we already know it is at least one
    return len(text) == count


def matches(pattern: str, value: str) -> bool:
    """Whether ``pattern`` is consistent with ``value``, i.e. whether ``pattern ∈ P(value)``.

    Matching is token-wise: both sides are tokenized with :func:`tokenize` and
    the pattern's parts are matched against the value's tokens one for one. A
    ``{k}`` part matches a token of exactly ``k`` characters of that class, and
    a ``+`` part matches a token of one or more -- the semantics recommended by
    paper-spec Section 8.1.
    """
    tokens = tokenize(value)
    parts = _parse(pattern)
    if len(parts) != len(tokens):
        return False
    for (kind, cls, count), token in zip(parts, tokens, strict=True):
        if kind == "literal":
            if token.text != cls:
                return False
        elif not _part_matches(cls, count, token.text):
            return False
    return True

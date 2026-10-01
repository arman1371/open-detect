"""Unit tests for the generalization hierarchy and P(v) (paper Section 2.1)."""

from __future__ import annotations

import pytest

from unidetect.algorithms.auto_validate.hierarchy import (
    ROOT_PATTERN,
    generalize,
    matches,
    token_count,
    tokenize,
)
from unidetect.algorithms.auto_validate.patterns import (
    DEFAULT_MAX_PATTERNS,
    iter_patterns,
    patterns_of,
    sorted_patterns,
)

# The patterns the paper lists for P("9:07") in Section 2.1. Two of them
# ("<digit>:07" and "9:<digit>{2}") appear as commented-out drafts in the
# camera-ready TeX; both are genuine generalizations of "9:07" and are
# produced here.
PAPER_PATTERNS_9_07 = (
    "9:07",
    "<digit>:07",
    "9:<digit>{2}",
    "<digit>:<digit>{2}",
    "<digit>+:<digit>{2}",
    "<digit>:<digit>+",
    "<num>:<digit>+",
)


class TestTokenize:
    def test_splits_runs_of_digit_letter_and_symbol(self):
        tokens = tokenize("9:07")
        assert [(t.text, t.char_class) for t in tokens] == [
            ("9", "digit"),
            (":", "symbol"),
            ("07", "digit"),
        ]

    def test_mixed_alphanumeric_run_is_alphanum(self):
        assert tokenize("a1")[0].char_class == "alphanum"

    def test_token_count_matches_run_definition(self):
        assert token_count("9:07") == 3
        assert token_count("02/18/2015") == 5
        assert token_count("0.1|02/18/2015 00:00:00|OnBooking") == 17

    def test_empty_value_has_no_tokens(self):
        assert tokenize("") == ()


class TestPatternsOf:
    @pytest.mark.parametrize("pattern", PAPER_PATTERNS_9_07)
    def test_paper_patterns_are_members_of_p_9_07(self, pattern):
        assert pattern in patterns_of("9:07")

    def test_root_pattern_is_never_generated(self):
        for value in ("9:07", "abc", "", "12/31/2020", "N/A"):
            assert ROOT_PATTERN not in patterns_of(value)

    def test_patterns_are_hashable_and_deterministic(self):
        first = patterns_of("9:07")
        second = patterns_of("9:07")
        assert first == second
        assert len({*first}) == len(first)
        assert sorted_patterns(first) == sorted_patterns(second)

    def test_ordering_is_coarsest_first(self):
        ordered = sorted_patterns(patterns_of("9:07"))
        from unidetect.algorithms.auto_validate.hierarchy import generality_weight

        weights = [generality_weight(p) for p in ordered]
        assert weights == sorted(weights)

    def test_contains_the_value_itself(self):
        assert "9:07" in patterns_of("9:07")

    def test_tau_prunes_wide_values(self):
        wide = "1|2|3|4|5|6|7|8|9"
        # digit, symbol, digit, ... -> 17 tokens
        assert token_count(wide) == 17
        assert patterns_of(wide, tau=8) == frozenset()
        assert patterns_of(wide, tau=32) != frozenset()

    def test_long_value_stays_bounded(self):
        value = "123-456-7890/" * 3
        assert len(patterns_of(value, 32)) <= DEFAULT_MAX_PATTERNS

    def test_generation_terminates_on_wide_value(self):
        wide = "1|2|3|4|5|6|7|8|9|10"
        emitted = list(iter_patterns(wide))
        assert len(emitted) == len(set(emitted))
        assert len(emitted) <= DEFAULT_MAX_PATTERNS + 2

    def test_hierarchy_endpoints_survive_truncation(self):
        value = "0.1|02/18/2015 00:00:00|OnBooking"
        patterns = patterns_of(value, 32)
        assert value in patterns
        assert generalize(tokenize(value)) in patterns


class TestGeneralize:
    def test_coarsest_form_matches_the_paper_datetime_example(self):
        # The paper's own coarse output for a date-time column
        # (Section 2.1): "<num>/<num>/<num> <num>:<num>:<num> <letter>+".
        assert generalize(tokenize("02/18/2015 10:30:45 AM")) == (
            "<num>/<num>/<num> <num>:<num>:<num> <letter>+"
        )

    def test_symbols_stay_literal_in_the_coarse_form(self):
        assert generalize(tokenize("9:07")) == "<num>:<num>"


class TestMatching:
    @pytest.mark.parametrize(
        "pattern,value,expected",
        [
            # bare class == exactly one character
            ("<digit>", "9", True),
            ("<digit>", "90", False),
            ("<letter>", "a", True),
            ("<letter>", "ab", False),
            ("<symbol>", ":", True),
            # {k} == exactly k characters
            ("<digit>{2}", "07", True),
            ("<digit>{2}", "7", False),
            ("<digit>{2}", "007", False),
            ("<alphanum>{2}", "ab", True),
            ("<alphanum>{2}", "a1", True),
            ("<alphanum>{2}", "abc", False),
            # + == one or more
            ("<digit>+", "7", True),
            ("<digit>+", "907", True),
            ("<letter>+", "OnBooking", True),
            ("<letter>+", "12", False),
            # <num> covers a whole numeric run
            ("<num>", "2015", True),
            ("<num>", "2015x", False),
            # mixed patterns
            ("<digit>:<digit>{2}", "9:07", True),
            ("<num>:<digit>+", "9:07", True),
            # literal patterns are exact
            ("9:07", "9:07", True),
            ("9:07", "9:8", False),
            ("9:07", "19:07", False),
        ],
    )
    def test_matching_semantics(self, pattern, value, expected):
        assert matches(pattern, value) is expected

    @pytest.mark.parametrize("pattern", PAPER_PATTERNS_9_07)
    def test_every_paper_pattern_matches_its_own_value(self, pattern):
        assert matches(pattern, "9:07")

    def test_token_count_must_agree(self):
        assert not matches("<digit>", "9:07")

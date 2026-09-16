"""Unit tests for text_utils.py."""

from __future__ import annotations

from unidetect.text_utils import is_float_like, is_integer_like, is_mixed_alphanumeric, tokenize


class TestIntegerLike:
    def test_positive(self):
        assert is_integer_like("123")

    def test_negative(self):
        assert is_integer_like("-45")

    def test_rejects_float(self):
        assert not is_integer_like("1.5")

    def test_rejects_text(self):
        assert not is_integer_like("abc")


class TestFloatLike:
    def test_plain_float(self):
        assert is_float_like("3.14")

    def test_scientific_notation(self):
        assert is_float_like("1.5e10")

    def test_integer_is_also_float_like(self):
        assert is_float_like("42")

    def test_rejects_text(self):
        assert not is_float_like("abc")


class TestMixedAlphanumeric:
    def test_code_like_value(self):
        assert is_mixed_alphanumeric("SKU-9981")

    def test_pure_letters_rejected(self):
        assert not is_mixed_alphanumeric("Paris")

    def test_pure_digits_rejected(self):
        assert not is_mixed_alphanumeric("12345")


class TestTokenize:
    def test_splits_on_whitespace_and_punctuation(self):
        assert tokenize("Kevin Doeling, PhD.") == ["Kevin", "Doeling", "PhD"]

    def test_empty_string(self):
        assert tokenize("") == []

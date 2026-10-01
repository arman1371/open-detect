"""Unit tests for AutoValidateConfig validation (no Spark required)."""

from __future__ import annotations

from dataclasses import FrozenInstanceError

import pytest

from unidetect.algorithms.auto_validate.config import AutoValidateConfig
from unidetect.exceptions import ConfigurationError


class TestDefaults:
    def test_matches_paper_defaults(self):
        config = AutoValidateConfig()
        assert config.variant == "fmdv_vh"
        assert config.r == 0.05
        assert config.m == 100
        assert config.tau == 8
        assert config.theta == 0.1
        assert config.drift_significance == 0.01

    def test_is_frozen(self):
        config = AutoValidateConfig()
        with pytest.raises(FrozenInstanceError, match="cannot assign to field"):
            config.r = 0.5  # type: ignore[misc]

    @pytest.mark.parametrize(
        "variant,vertical,horizontal",
        [
            ("fmdv", False, False),
            ("fmdv_v", True, False),
            ("fmdv_h", False, True),
            ("fmdv_vh", True, True),
        ],
    )
    def test_variant_cut_flags(self, variant, vertical, horizontal):
        config = AutoValidateConfig(variant=variant)
        assert config.uses_vertical_cuts is vertical
        assert config.uses_horizontal_cuts is horizontal


class TestValidation:
    def test_rejects_unknown_variant(self):
        with pytest.raises(ConfigurationError, match="variant"):
            AutoValidateConfig(variant="fmdv_x")

    @pytest.mark.parametrize("name", ["r", "theta", "drift_significance"])
    @pytest.mark.parametrize("value", [-0.1, 1.1, 2.0])
    def test_rejects_out_of_range_fractions(self, name, value):
        with pytest.raises(ConfigurationError, match=name):
            AutoValidateConfig(**{name: value})

    @pytest.mark.parametrize("name", ["r", "theta", "drift_significance"])
    @pytest.mark.parametrize("value", [0.0, 0.5, 1.0])
    def test_accepts_fractions_in_unit_range(self, name, value):
        config = AutoValidateConfig(**{name: value})
        assert getattr(config, name) == value

    @pytest.mark.parametrize("value", [0, -1])
    def test_rejects_m_below_one(self, value):
        with pytest.raises(ConfigurationError, match="m"):
            AutoValidateConfig(m=value)

    @pytest.mark.parametrize("value", [0, -3])
    def test_rejects_tau_below_one(self, value):
        with pytest.raises(ConfigurationError, match="tau"):
            AutoValidateConfig(tau=value)

    def test_accepts_smallest_valid_thresholds(self):
        config = AutoValidateConfig(m=1, tau=1)
        assert (config.m, config.tau) == (1, 1)

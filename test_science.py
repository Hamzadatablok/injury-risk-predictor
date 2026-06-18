"""
Unit tests for the scientific logic.
Run with:  pytest -v
"""

import pytest

from science import compute_acwr, compute_risk


# ---------- compute_acwr tests ----------

def test_acwr_balanced_load_is_sweet_spot():
    """A constant load should give ACWR=1.0 and the sweet spot."""
    result = compute_acwr([300] * 28)
    assert result["acwr"] == 1.0
    assert result["acwr_zone"] == "sweet_spot"


def test_acwr_spike_is_danger():
    """A sudden load spike should fall into the danger zone."""
    loads = [200] * 21 + [600] * 7   # 21 light days then 7 heavy days
    result = compute_acwr(loads)
    assert result["acwr"] > 1.5
    assert result["acwr_zone"] == "danger"


def test_acwr_too_few_days_raises_error():
    """Fewer than 7 days should raise an error."""
    with pytest.raises(ValueError):
        compute_acwr([100, 200, 300])


# ---------- compute_risk tests ----------

def test_risk_healthy_athlete_is_low():
    """Healthy athlete: balanced load, good sleep, no injuries."""
    result = compute_risk(acwr=1.0, sleep=8, resting_hr=55)
    assert result["risk_level"] == "low"
    assert result["risk_score"] == 0


def test_risk_stressed_athlete_is_critical():
    """Stressed athlete: all factors bad -> critical risk."""
    result = compute_risk(acwr=1.6, sleep=5.5, resting_hr=74,
                          previous_injuries=2, soreness=8)
    assert result["risk_level"] == "critical"
    assert result["risk_score"] == 100


def test_risk_score_never_exceeds_100():
    """Risk score must never exceed 100 no matter how bad the factors."""
    result = compute_risk(acwr=3.0, sleep=2, resting_hr=99,
                          previous_injuries=5, soreness=10)
    assert result["risk_score"] <= 100

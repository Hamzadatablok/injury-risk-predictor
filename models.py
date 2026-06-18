"""
Pydantic data models.
Defines the system's input schema and the structured output schema
for each agent, guaranteeing clean, validated data throughout.
"""

from typing import List
from enum import Enum
from pydantic import BaseModel, Field


# ===== Input: athlete profile =====
class AthleteProfile(BaseModel):
    name: str
    age: int = Field(..., ge=10, le=80)
    sport: str
    daily_loads: List[float] = Field(..., min_length=7)
    avg_sleep_hours: float = Field(..., ge=0, le=14)
    resting_hr: int = Field(..., ge=30, le=120)
    previous_injuries: int = Field(0, ge=0)
    soreness_1_to_10: int = Field(0, ge=0, le=10)


# ===== Constrained risk values =====
class RiskLevel(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    HIGH = "high"
    CRITICAL = "critical"


# ===== Agent 1 output =====
class WorkloadAnalysis(BaseModel):
    acute_load: float
    chronic_load: float
    acwr: float
    acwr_zone: str
    notes: str


# ===== Agent 2 output =====
class InjuryRiskAssessment(BaseModel):
    risk_level: RiskLevel
    risk_score_0_100: int = Field(..., ge=0, le=100)
    key_factors: List[str]
    rationale: str


# ===== Agent 3 output =====
class PreventionPlan(BaseModel):
    summary: str
    recommendations: List[str]
    load_adjustment: str
    monitoring: List[str]
    disclaimer: str = "Educational assessment, not a medical diagnosis."

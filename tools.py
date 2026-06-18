"""
CrewAI tools — wrap our scientific logic so agents can call it.
Each tool = name + description + input schema + a _run method.
"""

import json
from typing import List, Type

from pydantic import BaseModel, Field
from crewai.tools import BaseTool

from science import compute_acwr, compute_risk


# ---------- Tool 1: ACWR calculator ----------

class ACWRInput(BaseModel):
    """Tool input schema — tells the agent what to send."""
    daily_loads: List[float] = Field(..., description="List of daily training loads")


class ACWRTool(BaseTool):
    name: str = "acwr_calculator"
    description: str = (
        "Compute the Acute:Chronic Workload Ratio (ACWR) and its zone "
        "from a list of daily training loads."
    )
    args_schema: Type[BaseModel] = ACWRInput

    def _run(self, daily_loads: List[float]) -> str:
        result = compute_acwr(daily_loads)
        return json.dumps(result, ensure_ascii=False)


# ---------- Tool 2: risk scorer ----------

class RiskInput(BaseModel):
    acwr: float = Field(..., description="The computed ACWR value")
    sleep: float = Field(..., description="Average sleep hours")
    resting_hr: int = Field(..., description="Resting heart rate")
    previous_injuries: int = Field(0, description="Number of previous injuries")
    soreness: int = Field(0, description="Muscle soreness level 0-10")


class RiskTool(BaseTool):
    name: str = "risk_scorer"
    description: str = (
        "Compute an injury risk score (0-100) and its level by combining "
        "ACWR, sleep, resting HR, previous injuries and muscle soreness."
    )
    args_schema: Type[BaseModel] = RiskInput

    def _run(self, acwr: float, sleep: float, resting_hr: int,
             previous_injuries: int = 0, soreness: int = 0) -> str:
        result = compute_risk(acwr, sleep, resting_hr,
                              previous_injuries, soreness)
        return json.dumps(result, ensure_ascii=False)

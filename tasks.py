"""
The three tasks — each bound to an agent and a structured output schema.
output_pydantic guarantees the result matches our models (Structured Output).
"""

from crewai import Task

from models import WorkloadAnalysis, InjuryRiskAssessment, PreventionPlan
from agents import workload_analyst, risk_assessor, prevention_advisor


def build_tasks(athlete_json: str):
    """Build the three tasks and pass in the athlete data."""

    analyze_task = Task(
        description=(
            "Analyze the training load for the following athlete.\n"
            f"Athlete data (JSON):\n{athlete_json}\n\n"
            "Use the acwr_calculator tool on the daily_loads list. "
            "Return the acute and chronic loads, the ACWR and its zone, with notes."
        ),
        expected_output="A structured workload analysis matching the WorkloadAnalysis schema.",
        agent=workload_analyst,
        output_pydantic=WorkloadAnalysis,
    )

    assess_task = Task(
        description=(
            "Based on the previous workload analysis and the athlete data:\n"
            f"{athlete_json}\n\n"
            "Use the risk_scorer tool (pass acwr from the analysis, sleep, "
            "resting_hr, previous_injuries, soreness). "
            "Produce the risk level and score with the factors and rationale."
        ),
        expected_output="A structured risk assessment matching the InjuryRiskAssessment schema.",
        agent=risk_assessor,
        context=[analyze_task],
        output_pydantic=InjuryRiskAssessment,
    )

    plan_task = Task(
        description=(
            "Based on the risk assessment, write a concise, practical prevention plan: "
            "summary, actionable recommendations, a suggested load adjustment, "
            "and metrics to monitor this week. Avoid any medical diagnosis."
        ),
        expected_output="A structured prevention plan matching the PreventionPlan schema.",
        agent=prevention_advisor,
        context=[analyze_task, assess_task],
        output_pydantic=PreventionPlan,
    )

    return [analyze_task, assess_task, plan_task]

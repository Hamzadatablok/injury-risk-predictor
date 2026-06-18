"""
Assemble the agents and tasks into a sequential Crew.
"""

from crewai import Crew, Process

from agents import workload_analyst, risk_assessor, prevention_advisor
from tasks import build_tasks


def build_crew(athlete_json: str) -> Crew:
    return Crew(
        agents=[workload_analyst, risk_assessor, prevention_advisor],
        tasks=build_tasks(athlete_json),
        process=Process.sequential,  # analyze -> assess -> plan
        verbose=True,
    )

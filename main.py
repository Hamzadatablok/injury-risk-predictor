"""
Project entry point.
  python main.py                 # uses athlete.json
  python main.py my_athlete.json # uses your own file
"""

import sys
import json

from models import AthleteProfile, PreventionPlan
from crew import build_crew


def load_athlete(path: str) -> AthleteProfile:
    """Read the athlete data and validate it through Pydantic."""
    with open(path, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return AthleteProfile(**raw)


def main() -> None:
    path = sys.argv[1] if len(sys.argv) > 1 else "athlete.json"

    athlete = load_athlete(path)
    print(f"\n🏃 Analyzing athlete: {athlete.name} — {athlete.sport}\n")

    # Run the crew
    crew = build_crew(athlete.model_dump_json())
    result = crew.kickoff()

    # Print the final structured report
    plan: PreventionPlan = result.pydantic
    print("\n" + "=" * 55)
    print("📋 Final Prevention Plan")
    print("=" * 55)
    print(json.dumps(plan.model_dump(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

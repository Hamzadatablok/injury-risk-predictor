"""
Definition of the three agents.
Each agent = role + goal + backstory (+ tools if needed).
"""

import os
from dotenv import load_dotenv
from crewai import Agent, LLM

from tools import ACWRTool, RiskTool

# Load the API key from the .env file
load_dotenv()

# Shared LLM for all agents — via OpenRouter
# (low temperature = consistent answers, suitable for health applications)
llm = LLM(
    model=os.getenv("MODEL_NAME", "openrouter/openai/gpt-4o-mini"),
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0.2,
)

# Instantiate the tools once
acwr_tool = ACWRTool()
risk_tool = RiskTool()


# ---------- Agent 1: workload analyst ----------
workload_analyst = Agent(
    role="Sports Training Load Analyst",
    goal="Accurately compute the ACWR and determine the load zone from athlete data",
    backstory=(
        "An expert in training science and exercise physiology. You always "
        "rely on tools and numbers, never guessing. You use the acwr_calculator tool."
    ),
    tools=[acwr_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


# ---------- Agent 2: risk assessor ----------
risk_assessor = Agent(
    role="Injury Risk Assessment Specialist",
    goal="Combine all factors into a scientifically grounded risk score and level",
    backstory=(
        "A specialist in sports medicine and prevention. You take the workload "
        "analysis and other factors (sleep, HR, previous injuries) and use the "
        "risk_scorer tool."
    ),
    tools=[risk_tool],
    llm=llm,
    verbose=True,
    allow_delegation=False,
)


# ---------- Agent 3: prevention advisor ----------
prevention_advisor = Agent(
    role="Prevention and Load Management Advisor",
    goal="Turn the assessment into a practical, clear prevention plan for athlete and coach",
    backstory=(
        "A fitness coach and rehabilitation specialist with field experience. "
        "You translate numbers into simple, actionable recommendations, while "
        "avoiding any medical claims."
    ),
    llm=llm,
    verbose=True,
    allow_delegation=False,
)

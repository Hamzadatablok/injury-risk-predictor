# 🏥 Injury Risk Assessment — Multi-Agent AI System

A multi-agent AI system (CrewAI) that assesses athlete injury risk using real
sports-science metrics (Acute:Chronic Workload Ratio) and produces a structured,
validated prevention plan.

---

## 🧠 Architecture

Three agents run sequentially, each returning structured (Pydantic) output:

```
AthleteProfile (JSON)
        │
        ▼
┌────────────────────┐   🔧 acwr_calculator
│ 1. Workload Analyst │ ───────────────────►  WorkloadAnalysis
└─────────┬──────────┘
          ▼
┌────────────────────┐   🔧 risk_scorer
│ 2. Risk Assessor    │ ───────────────────►  InjuryRiskAssessment
└─────────┬──────────┘
          ▼
┌────────────────────┐
│ 3. Prevention Advisor│ ──────────────────►  PreventionPlan ✅
└────────────────────┘
```

**Core idea:** the agent (LLM) decides *when* to compute, but the actual
calculation is done by precise, deterministic tools — no guessed numbers.

---

## 🔬 The Science

`ACWR = acute load (7 days) ÷ chronic load (28 days)`

| Zone | ACWR | Meaning |
|------|------|---------|
| Undertraining | < 0.80 | Loss of fitness |
| Sweet spot ✅ | 0.80–1.30 | Safe training load |
| Danger ⚠️ | > 1.50 | Elevated injury risk |

ACWR is combined with sleep, resting HR, previous injuries and muscle
soreness into a 0–100 risk score.

---

## 🛠️ Tech Stack

- **CrewAI** — multi-agent orchestration
- **Pydantic** — data validation and structured output
- **OpenRouter** — access to large language models (LLMs)
- **pytest** — unit tests for the scientific logic

---

## 🚀 Quick Start

```bash
# 1) Virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 2) Install
pip install -r requirements.txt

# 3) API key
copy .env.example .env         # then add your OpenRouter key

# 4) Run
python main.py                 # uses athlete.json
python main.py my_athlete.json # your own data

# 5) Tests
pytest -v
```

---

## 📂 Structure

| File | Role |
|------|------|
| `models.py` | Pydantic models (input + structured output) |
| `science.py` | Scientific logic: ACWR and risk score |
| `test_science.py` | Unit tests for the scientific logic |
| `tools.py` | Wraps the logic as CrewAI tools |
| `agents.py` | Definition of the three agents |
| `tasks.py` / `crew.py` | Tasks and crew assembly |
| `main.py` | Entry point |

---

## ⚠️ Disclaimer

This is an educational project, not a medical diagnostic tool.

---

## 👤 Author

**Hamza Elouahdani** — Data Scientist & Sports Performance Specialist

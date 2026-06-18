# 🏥 Injury Risk Assessment — Multi-Agent AI System

نظام **وكلاء ذكاء اصطناعي متعدّد (Multi-Agent)** يحلّل بيانات الرياضي ويقدّر خطر الإصابة
بناءً على علم رياضي حقيقي (نسبة الحِمل الحاد:المزمن **ACWR**)، ثم يقترح خطة وقاية عملية.

> A multi-agent AI system (CrewAI) that assesses athlete injury risk using
> real sports-science metrics (Acute:Chronic Workload Ratio) and produces a
> structured, validated prevention plan.

---

## 🧠 المعمارية | Architecture

ثلاثة وكلاء يعملون بالتسلسل، كل واحد يُرجع مخرجات منظَّمة (Pydantic):

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

**الفكرة الأساسية:** الوكيل (LLM) يقرّر *متى* يحسب، لكن الحساب الفعلي يتم بأدوات
علمية دقيقة (deterministic) — لا تخمين للأرقام.

---

## 🔬 العلم | The Science

`ACWR = الحِمل الحاد (7 أيام) ÷ الحِمل المزمن (28 يوماً)`

| Zone | ACWR | الدلالة |
|------|------|---------|
| Undertraining | < 0.80 | نقص تدريب |
| Sweet spot ✅ | 0.80–1.30 | حِمل آمن |
| Danger ⚠️ | > 1.50 | خطر إصابة مرتفع |

تُدمج ACWR مع النوم ونبض الراحة والإصابات السابقة والإجهاد العضلي في درجة خطر 0–100.

---

## 🛠️ التقنيات | Tech Stack

- **CrewAI** — تنسيق الوكلاء المتعدّدين
- **Pydantic** — التحقق من البيانات والمخرجات المنظَّمة
- **OpenRouter** — الوصول إلى نماذج اللغة (LLM)
- **pytest** — اختبارات الوحدة للمنطق العلمي

---

## 🚀 التشغيل | Quick Start

```bash
# 1) البيئة الافتراضية
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS / Linux

# 2) التثبيت
pip install -r requirements.txt

# 3) المفتاح
copy .env.example .env         # ثم ضع مفتاح OpenRouter بداخله

# 4) التشغيل
python main.py                 # يستخدم athlete.json
python main.py my_athlete.json # بياناتك الخاصة

# 5) الاختبارات
pytest -v
```

---

## 📂 الهيكل | Structure

| File | Role |
|------|------|
| `models.py` | نماذج Pydantic (مدخلات + مخرجات منظَّمة) |
| `science.py` | المنطق العلمي: ACWR ودرجة الخطر |
| `test_science.py` | اختبارات وحدة للمنطق العلمي |
| `tools.py` | تغليف المنطق كأدوات CrewAI |
| `agents.py` | تعريف الوكلاء الثلاثة |
| `tasks.py` / `crew.py` | المهام وتجميع الفريق |
| `main.py` | نقطة التشغيل |

---

## ⚠️ تنبيه | Disclaimer

هذا المشروع **تعليمي** وليس أداة تشخيص طبي.
This is an educational project, not a medical diagnostic tool.

---

## 👤 المؤلف | Author

**Hamza Elouahdani** — Data Scientist & Sports Performance Specialist

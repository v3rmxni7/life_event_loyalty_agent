# life_event_loyalty_agent
Overview

This project is an agentic AI proof-of-concept that goes beyond traditional churn detection.

Instead of merely identifying that a customer stopped shopping, the system infers why their behavior changed (life events, financial stress, health shifts) and prescribes loyalty actions mapped directly to Antavo concepts (Clubs, Rewards, Campaigns).

Core idea:
“Don’t just track what customers buy. Track who they are becoming.”

This aligns directly with Antavo’s vision of Agentic Loyalty, where AI acts as a strategic co-pilot, not a reporting tool.

What Problem This Solves

Most loyalty platforms stop at:

Descriptive analytics (“purchase frequency dropped”)

Generic win-back campaigns (“10% off”)

This system delivers:

Causal reasoning → Why did behavior change?

Prescriptive output → What should we do next?

Human-in-the-loop safety → AI recommends, humans approve

Core Capabilities
1️⃣ Deterministic Behavior Analysis (No Hallucination)

Category disappearance & emergence

Velocity change (frequency drop)

Quality shift (Premium → Value)

Signals extracted using Python (not LLMs)

2️⃣ Probabilistic Life-Event Inference (Agentic AI)

Uses an LLM only after facts are established

Generates:

Primary hypothesis

Alternative hypotheses

Confidence score

Supporting evidence

Business risk framing

3️⃣ Prescriptive Loyalty Strategy (Antavo-Native)

Maps diagnosis to:

Clubs

Rewards

Channels

Guardrails (what NOT to do)

Outputs an Antavo-ready API payload (simulated)

4️⃣ Human Approval Loop

AI does not auto-execute

Strategy is reviewed & approved before “push to Antavo”

Prevents “creepy AI” failure modes

High-Level Architecture
                    ┌────────────────────────┐
                    │   Customer Data Input  │
                    │ (Receipts, Feedback)   │
                    └───────────┬────────────┘
                                │
                                ▼
┌──────────────────────────────────────────────────┐
│  Agent 1: Behavior Agent (Deterministic Layer)   │
│--------------------------------------------------│
│ • Category shifts                                │
│ • Velocity trends                                │
│ • Premium → Value quality change                 │
│ • Pure Python / Pandas logic                     │
└───────────┬──────────────────────────────────────┘
            │  (Structured Signals)
            ▼
┌──────────────────────────────────────────────────┐
│  Agent 2: Life Event Agent (Reasoning Layer)     │
│--------------------------------------------------│
│ • LLM-powered hypothesis generation              │
│ • Primary + alternative explanations             │
│ • Confidence scoring                             │
│ • Business risk articulation                     │
└───────────┬──────────────────────────────────────┘
            │  (Diagnosis)
            ▼
┌──────────────────────────────────────────────────┐
│  Agent 3: Loyalty Strategy Agent (Action Layer)  │
│--------------------------------------------------│
│ • Maps insight → Antavo features                 │
│ • Clubs, rewards, channels                       │
│ • Prohibited actions (guardrails)                │
│ • Antavo API payload (simulated)                 │
└───────────┬──────────────────────────────────────┘
            │
            ▼
┌──────────────────────────────────────────────────┐
│  Streamlit UI (Human-in-the-Loop Copilot)        │
│--------------------------------------------------│
│ • Evidence view                                  │
│ • Agent reasoning trace                          │
│ • Loyalty strategy preview                       │
│ • “Approve & Push” simulation                    │
└──────────────────────────────────────────────────┘

Why This Architecture Matters
Design Choice	Why It’s Enterprise-Grade
Deterministic → Probabilistic	Prevents LLM hallucination
Multi-agent separation	Mirrors real org roles (Analyst → Strategist)
API-first outputs	Matches Antavo’s headless architecture
Human approval	Aligns with enterprise trust & compliance
Synthetic data	Zero PII risk, demo-safe
Example Use Cases (Supermarket)

New Parent / Pregnancy shift
→ Remove alcohol offers, add free delivery & family club

Inflation / Budget stress
→ Avoid luxury upsells, promote value bundles

Health-driven lifestyle change
→ Transition to wellness-focused loyalty journeys

Project Structure
life_event_loyalty_agent/
├── app.py                     # Streamlit copilot UI
├── src/
│   ├── pipeline.py            # Agent orchestration
│   ├── agents/
│   │   ├── behavior_agent.py
│   │   ├── life_event_agent.py
│   │   └── loyalty_strategy_agent.py
│   ├── llm/
│   │   └── groq_client.py
│   └── utils/
│       └── json_utils.py
├── data/
│   ├── customers/
│   │   ├── sarah.json
│   │   ├── mike_inflation.json
│   │   └── alex_health.json
│   └── taxonomy.json
└── README.md

Running the App
source .venv/bin/activate
export GROQ_API_KEY="your_key_here"
streamlit run app.py

How This Fits Antavo’s Roadmap

Demonstrates Agentic AI beyond chatbots

Complements Timi AI with causal + prescriptive reasoning

Produces ready-to-execute loyalty workflows

Scales naturally across verticals (retail, grocery, QSR)

This POC shows how Antavo can evolve from:

“Loyalty platform” → “Autonomous loyalty intelligence layer”

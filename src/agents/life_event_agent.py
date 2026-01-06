# src/agents/life_event_agent.py

import json
from src.llm.groq_client import GroqClient
from src.utils.json_utils import clean_llm_json


class LifeEventAgent:
    """
    Probabilistic reasoning agent.
    Infers likely lifestyle / life-event shifts from behavioral signals.
    """

    def __init__(self):
        self.llm = GroqClient()

    def infer(self, behavior_signals: dict, feedback: list) -> dict:
        prompt = f"""
You are a behavioral intelligence agent for a retail loyalty platform.

You are given:
1. Deterministic behavioral signals (FACTS, do not invent):
{json.dumps(behavior_signals, indent=2)}

2. Customer feedback:
{json.dumps(feedback, indent=2)}

Your task:
- Identify the most likely lifestyle or life-event shift.
- Consider at least ONE alternative hypothesis.
- Explicitly reject weak alternatives.
- Estimate confidence.
- Explain business risk if no action is taken.

IMPORTANT:
- Do NOT infer sensitive personal attributes.
- Frame insights as lifestyle or situational shifts.
- Output MUST be strict JSON only.

Return EXACTLY this schema:

{{
  "primary_hypothesis": "string",
  "alternative_hypotheses": [
    {{
      "hypothesis": "string",
      "reason_rejected": "string"
    }}
  ],
  "confidence": "High | Medium | Low",
  "evidence": ["string"],
  "business_risk": "string"
}}
"""

        raw = self.llm.run(prompt)
        cleaned = clean_llm_json(raw)

        return json.loads(cleaned)

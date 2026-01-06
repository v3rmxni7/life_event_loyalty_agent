# src/agents/loyalty_strategy_agent.py

import json
from src.llm.groq_client import GroqClient
from src.utils.json_utils import clean_llm_json


class LoyaltyStrategyAgent:
    """
    Prescriptive agent.
    Translates a diagnosis into Antavo-native loyalty actions.
    """

    def __init__(self):
        self.llm = GroqClient()

    def design(self, diagnosis: dict, customer_id: str) -> dict:
        """
        diagnosis: output from LifeEventAgent
        customer_id: string
        """

        prompt = f"""
You are a Senior Loyalty Architect working on Antavo.

A customer has been analyzed with the following diagnosis:
{json.dumps(diagnosis, indent=2)}

Your task is to design a SAFE, EMPATHETIC, and BUSINESS-EFFECTIVE
loyalty intervention using Antavo concepts.

IMPORTANT RULES:
- Do NOT mention sensitive personal conditions directly.
- Do NOT shame or alarm the customer.
- Prefer SERVICE or ACCESS rewards over DISCOUNTS.
- Include explicit prohibited actions.
- Output MUST be valid JSON ONLY.

Return EXACTLY this schema:

{{
  "segment": "string",
  "club_action": {{
    "action": "Invite | Update | None",
    "club_name": "string"
  }},
  "rewards": [
    {{
      "type": "Service | Access | Points",
      "description": "string",
      "duration": "string",
      "business_rationale": "string"
    }}
  ],
  "channels": ["Email", "Push", "SMS"],
  "message_tone": "Supportive | Informational | Neutral",
  "example_message": "string",
  "guardrails": "string",
  "prohibited_actions": [
    "string"
  ],
  "antavo_api_payload": {{
    "endpoint": "/events/trigger",
    "method": "POST",
    "body": {{
      "customer_id": "{customer_id}",
      "event": "life_event_loyalty_intervention",
      "workflow_id": "life_event_retention_v1",
      "metadata": {{
        "segment": "string",
        "club": "string",
        "reason": "string"
      }}
    }}
  }}
"""
        raw_output = self.llm.run(prompt)
        cleaned = clean_llm_json(raw_output)

        return json.loads(cleaned)

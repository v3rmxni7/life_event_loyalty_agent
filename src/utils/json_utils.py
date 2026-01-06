# src/utils/json_utils.py

import re


def clean_llm_json(raw_output: str) -> str:
    """
    Cleans LLM output by extracting the first valid JSON object.
    Handles cases where the model adds markdown or prose.
    """

    if not raw_output:
        raise ValueError("Empty LLM output")

    # Remove markdown code fences if present
    cleaned = re.sub(r"```json|```", "", raw_output).strip()

    # Extract JSON block
    match = re.search(r"\{.*\}", cleaned, re.DOTALL)

    if not match:
        raise ValueError("No valid JSON object found in LLM output")

    return match.group(0)

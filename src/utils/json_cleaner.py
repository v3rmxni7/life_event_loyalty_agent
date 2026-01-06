def clean_llm_json(text: str) -> str:
    """
    Extract JSON object from LLM output.
    """
    if not text:
        return ""

    text = text.strip()

    # Remove markdown fences
    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "").strip()

    # Try to extract JSON substring
    start = text.find("{")
    end = text.rfind("}")

    if start != -1 and end != -1:
        return text[start : end + 1]

    return ""

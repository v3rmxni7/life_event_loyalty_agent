# src/agents/behavior_agent.py

from collections import Counter

# Keywords used to infer quality shifts
PREMIUM_KEYWORDS = [
    "organic", "premium", "artisan", "wagyu", "imported",
    "single origin", "fresh", "luxury"
]

VALUE_KEYWORDS = [
    "value", "basic", "store brand", "instant",
    "budget", "frozen", "economy"
]


class BehaviorAgent:
    """
    Deterministic agent.
    Extracts factual behavioral signals from purchase history.
    NO inference. NO guessing.
    """

    def analyze(self, purchase_history: dict) -> dict:
        """
        purchase_history: {
            "month_1": [{item, category}],
            "month_2": [...],
            "month_3": [...]
        }
        """

        month_1 = purchase_history.get("month_1", [])
        month_3 = purchase_history.get("month_3", [])

        # ----------------------------
        # Category presence analysis
        # ----------------------------
        categories_month_1 = {p["category"] for p in month_1}
        categories_month_3 = {p["category"] for p in month_3}

        disappeared_categories = categories_month_1 - categories_month_3
        emerged_categories = categories_month_3 - categories_month_1

        # ----------------------------
        # Velocity analysis
        # ----------------------------
        baseline_count = len(month_1)
        recent_count = len(month_3)

        if recent_count < baseline_count:
            velocity_trend = "Decreasing"
        elif recent_count > baseline_count:
            velocity_trend = "Increasing"
        else:
            velocity_trend = "Stable"

        # ----------------------------
        # Quality shift analysis
        # ----------------------------
        baseline_quality = self._classify_quality(month_1)
        recent_quality = self._classify_quality(month_3)

        if baseline_quality != recent_quality:
            quality_shift = f"{baseline_quality} → {recent_quality}"
        else:
            quality_shift = "Stable"

        # ----------------------------
        # Final deterministic output
        # ----------------------------
        return {
            "disappeared_categories": list(disappeared_categories),
            "emerged_categories": list(emerged_categories),
            "velocity_trend": velocity_trend,
            "quality_shift": quality_shift,
            "baseline_item_count": baseline_count,
            "recent_item_count": recent_count
        }

    def _classify_quality(self, items: list) -> str:
        """
        Classifies basket quality based on item name keywords.
        Returns: Premium | Value | Neutral
        """

        premium_hits = 0
        value_hits = 0

        for item in items:
            name = item["item"].lower()

            if any(k in name for k in PREMIUM_KEYWORDS):
                premium_hits += 1

            if any(k in name for k in VALUE_KEYWORDS):
                value_hits += 1

        if premium_hits > value_hits:
            return "Premium"
        if value_hits > premium_hits:
            return "Value"
        return "Neutral"

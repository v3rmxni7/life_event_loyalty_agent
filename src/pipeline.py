from src.agents.behavior_agent import BehaviorAgent
from src.agents.life_event_agent import LifeEventAgent
from src.agents.loyalty_strategy_agent import LoyaltyStrategyAgent

class LoyaltyPipeline:
    def __init__(self):
        self.behavior_agent = BehaviorAgent()
        self.life_event_agent = LifeEventAgent()
        self.strategy_agent = LoyaltyStrategyAgent()

    def run(self, customer_data: dict) -> dict:
        behavior_signals = self.behavior_agent.analyze(
            customer_data["purchase_history"]
        )

        diagnosis = self.life_event_agent.infer(
            behavior_signals,
            customer_data["feedback"]
        )

        strategy = self.strategy_agent.design(
            diagnosis=diagnosis,
            customer_id=customer_data["customer_id"]
        )

        return {
            "behavior_signals": behavior_signals,
            "diagnosis": diagnosis,
            "loyalty_strategy": strategy
        }

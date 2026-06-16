import json
from workspace_utilization_estimator.prompt_builder import PromptBuilder
from workspace_utilization_estimator.models.organization import Organization

class UtilizationResult:
    def __init__(
        self,
        low_estimate: float,
        most_likely_estimate: float,
        high_estimate: float,
        confidence_score: float,
        key_drivers: list[str],
        executive_summary: str,
    ):
        self.low_estimate = low_estimate
        self.most_likely_estimate = most_likely_estimate
        self.high_estimate = high_estimate
        self.confidence_score = confidence_score
        self.key_drivers = key_drivers
        self.executive_summary = executive_summary


class UtilizationAgent:
    """
    Phase 6: Takes an Organization, builds a prompt, calls an LLM,
    and returns a structured UtilizationResult.
    """

    def __init__(self, llm_client):
        """
        llm_client must expose a method:

            llm_client.generate(prompt: str) -> str

        returning a JSON string matching the schema defined in PromptBuilder.
        """
        self.llm_client = llm_client

    def estimate(self, organization: Organization) -> UtilizationResult:
        prompt = PromptBuilder(organization).build_prompt()
        raw_response = self.llm_client.generate(prompt)

        data = json.loads(raw_response)

        return UtilizationResult(
            low_estimate=data["low_estimate"],
            most_likely_estimate=data["most_likely_estimate"],
            high_estimate=data["high_estimate"],
            confidence_score=data["confidence_score"],
            key_drivers=data["key_drivers"],
            executive_summary=data["executive_summary"],
        )

class StubLLMClient:
    def generate(self, prompt: str) -> str:
        return json.dumps({
            "low_estimate": 0.55,
            "most_likely_estimate": 0.65,
            "high_estimate": 0.75,
            "confidence_score": 0.8,
            "key_drivers": [
                "High hybrid presence ratio",
                "Moderate meeting density"
            ],
            "executive_summary": "Utilization is moderate to high with strong hybrid patterns."
        })

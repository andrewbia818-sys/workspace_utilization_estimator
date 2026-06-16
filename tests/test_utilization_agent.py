from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.normalizer import Normalizer
from workspace_utilization_estimator.models.organization import Organization
from workspace_utilization_estimator.utilization_agent import UtilizationAgent, StubLLMClient

def test_utilization_agent_with_stub_llm():
    data = {
        "organization_name": "Acme Corp",
        "employees": 480,
        "sqft": 120000,
        "vacation_days": 18,
        "sick_days": 6,
        "travel_percentage": 10,
        "vpn_usage_percentage": 35,
        "peak_login_percentage": 65,
        "meeting_hours": 3.5,
        "hybrid_days": 3
    }

    client = ClientData.from_dict(data)
    proxy = Normalizer(client).to_proxy_data()
    org = Organization(client, proxy)

    agent = UtilizationAgent(StubLLMClient())
    result = agent.estimate(org)

    assert result.most_likely_estimate == 0.65
    assert result.confidence_score == 0.8
    assert "executive_summary" in result.__dict__
    assert "detailed_explanation" in result.__dict__
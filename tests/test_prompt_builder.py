from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.models.proxy_data import ProxyData
from workspace_utilization_estimator.models.organization import Organization
from workspace_utilization_estimator.prompt_builder import PromptBuilder

def test_prompt_builder_output():
    client = ClientData(
        organization_name="Acme Corp",
        employees=480,
        sqft=120000,
        vacation_days=18,
        sick_days=6,
        travel_percentage=10,
        vpn_usage_percentage=35,
        peak_login_percentage=65,
        meeting_hours=3.5,
        hybrid_days=3
    )

    proxy = ProxyData(
        avg_daily_presence=0.55,
        adjusted_vpn_factor=0.35,
        meeting_density_score=0.44,
        travel_absence_factor=0.10,
        hybrid_presence_ratio=0.60
    )

    org = Organization(client, proxy)
    builder = PromptBuilder(org)
    prompt = builder.build_prompt()

    assert "Acme Corp" in prompt
    assert "Avg Daily Presence" in prompt
    assert "Respond ONLY with valid JSON" in prompt
    assert '"estimated_utilization":' in prompt
    assert '"confidence":' in prompt
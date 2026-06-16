from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.models.proxy_data import ProxyData
from workspace_utilization_estimator.models.organization import Organization

def test_organization_model():
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

    summary = org.summary()
    assert summary["organization_name"] == "Acme Corp"
    assert summary["proxy_features"]["adjusted_vpn_factor"] == 0.35

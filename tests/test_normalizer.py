from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.normalizer import Normalizer

def test_normalizer_basic():
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
    norm = Normalizer(client)
    proxy = norm.to_proxy_data()

    assert 0 <= proxy.avg_daily_presence <= 1
    assert 0 <= proxy.adjusted_vpn_factor <= 1
    assert 0 <= proxy.meeting_density_score <= 1

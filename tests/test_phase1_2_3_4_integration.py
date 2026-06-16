from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness
from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.normalizer import Normalizer
from workspace_utilization_estimator.models.organization import Organization

def test_full_pipeline_phase1_2_3_4():
    data = load_client_json("workspace_utilization_estimator/sample_client.json")

    validate_client_data(data)
    check_reasonableness(data)

    client = ClientData.from_dict(data)
    proxy = Normalizer(client).to_proxy_data()

    org = Organization(client, proxy)

    assert org.client_data.organization_name == "Acme Corp"
    assert org.proxy_data.avg_daily_presence > 0
    assert org.proxy_data.adjusted_vpn_factor > 0
    assert org.proxy_data.meeting_density_score >= 0 and org.proxy_data.meeting_density_score <= 1
    assert org.proxy_data.travel_absence_factor >= 0 and org.proxy_data.travel_absence_factor <= 1
    assert org.proxy_data.hybrid_presence_ratio >=  0 and org.proxy_data.hybrid_presence_ratio <= 1
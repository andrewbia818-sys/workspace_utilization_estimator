from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness

def test_phase1_2_integration():
    data = load_client_json("sample_client.json")
    validate_client_data(data)
    check_reasonableness(data)

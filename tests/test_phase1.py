from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data


def test_phase1_end_to_end():
    data = load_client_json("sample_client.json")
    validate_client_data(data)

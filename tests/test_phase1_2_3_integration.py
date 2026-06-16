from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness
from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.normalizer import Normalizer

def test_full_pipeline():
    data = load_client_json("workspace_utilization_estimator/sample_client.json")
    validate_client_data(data)
    check_reasonableness(data)

    client = ClientData.from_dict(data)
    proxy = Normalizer(client).to_proxy_data()

    assert proxy is not None

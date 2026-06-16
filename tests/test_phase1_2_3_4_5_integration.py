from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness
from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.normalizer import Normalizer
from workspace_utilization_estimator.models.organization import Organization
from workspace_utilization_estimator.prompt_builder import PromptBuilder

def test_full_pipeline_phase1_to_5():
    data = load_client_json("workspace_utilization_estimator/sample_client.json")

    validate_client_data(data)
    check_reasonableness(data)

    client = ClientData.from_dict(data)
    proxy = Normalizer(client).to_proxy_data()
    org = Organization(client, proxy)

    prompt = PromptBuilder(org).build_prompt()

    assert "Raw Client Data" in prompt
    assert "Engineered Proxy Features" in prompt
    assert "Respond ONLY with valid JSON" in prompt
    assert '"estimated_utilization":' in prompt
    assert '"confidence":' in prompt
from workspace_utilization_estimator.parser import load_client_json

def test_load_client_json():
    data = load_client_json("sample_client.json")
    assert isinstance(data, dict)
    assert "vacation_days" in data
    assert "sick_days" in data
    assert "travel_percentage" in data
    assert "vpn_usage_percentage" in data
    assert "peak_login_percentage" in data
    assert "meeting_hours" in data
    assert "hybrid_days" in data

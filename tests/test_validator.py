from workspace_utilization_estimator.validator import validate_client_data

def test_valid_data():
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
    validate_client_data(data)

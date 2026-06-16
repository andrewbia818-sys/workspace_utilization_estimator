import pytest
from workspace_utilization_estimator.reasonableness import check_reasonableness

def test_reasonable_data_passes():
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
    check_reasonableness(data)  # should not raise

def test_unreasonable_sqft():
    data = {
        "organization_name": "Acme Corp",
        "employees": 480,
        "sqft": 1000,  # too small
        "vacation_days": 18,
        "sick_days": 6,
        "travel_percentage": 10,
        "vpn_usage_percentage": 35,
        "peak_login_percentage": 65,
        "meeting_hours": 3.5,
        "hybrid_days": 3
    }
    with pytest.raises(ValueError):
        check_reasonableness(data)

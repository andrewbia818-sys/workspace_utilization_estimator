CLIENT_ONBOARDING_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2020-12/schema",
    "type": "object",
    "properties": {
        "organization_name": {"type": "string"},
        "employees": {"type": "integer", "minimum": 1},
        "sqft": {"type": "integer", "minimum": 1},
        "vacation_days": {"type": "number", "minimum": 0},
        "sick_days": {"type": "number", "minimum": 0},
        "travel_percentage": {"type": "number", "minimum": 0, "maximum": 100},
        "vpn_usage_percentage": {"type": "number", "minimum": 0, "maximum": 100},
        "peak_login_percentage": {"type": "number", "minimum": 0, "maximum": 100},
        "meeting_hours": {"type": "number", "minimum": 0},
        "hybrid_days": {"type": "integer", "minimum": 0, "maximum": 7}
    },
    "required": [
        "organization_name",
        "employees",
        "sqft",
        "vacation_days",
        "sick_days",
        "travel_percentage",
        "vpn_usage_percentage",
        "peak_login_percentage",
        "meeting_hours",
        "hybrid_days"
    ],
    "additionalProperties": False
}

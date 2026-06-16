from jsonschema import validate, ValidationError

from workspace_utilization_estimator.schema import CLIENT_ONBOARDING_SCHEMA


def validate_client_data(data: dict) -> None:
    try:
        validate(instance=data, schema=CLIENT_ONBOARDING_SCHEMA)
    except ValidationError as e:
        raise ValueError(f"Invalid client input: {e.message}")

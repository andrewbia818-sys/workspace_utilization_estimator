from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness

def run(path: str):
    print(f"\nLoading: {path}")

    try:
        data = load_client_json(path)
        print("✓ JSON loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load JSON: {e}")
        return

    try:
        validate_client_data(data)
        print("✓ Schema validation passed")
    except Exception as e:
        print(f"❌ Schema validation failed: {e}")
        return

    try:
        check_reasonableness(data)
        print("✓ Reasonableness checks passed")
    except Exception as e:
        print(f"❌ Reasonableness check failed: {e}")
        return

    print("\nAll checks passed — input is valid and reasonable.")

if __name__ == "__main__":
    run("sample_client.json")

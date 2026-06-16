import argparse
from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness

def run_cli():
    parser = argparse.ArgumentParser(
        description="Workspace Utilization Estimator — Phase 1–2 Validation CLI"
    )

    parser.add_argument(
        "input_file",
        type=str,
        help="Path to the client JSON file"
    )

    args = parser.parse_args()
    path = args.input_file

    print(f"\n🔍 Loading: {path}")

    # Phase 1 — Load JSON
    try:
        data = load_client_json(path)
        print("✓ JSON loaded successfully")
    except Exception as e:
        print(f"❌ Failed to load JSON: {e}")
        return

    # Phase 1 — Schema Validation
    try:
        validate_client_data(data)
        print("✓ Schema validation passed")
    except Exception as e:
        print(f"❌ Schema validation failed: {e}")
        return

    # Phase 2 — Reasonableness Checks
    try:
        check_reasonableness(data)
        print("✓ Reasonableness checks passed")
    except Exception as e:
        print(f"❌ Reasonableness check failed: {e}")
        return

    print("\n🎉 All checks passed — input is valid and reasonable.")

if __name__ == "__main__":
    run_cli()

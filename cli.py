import argparse
from workspace_utilization_estimator.parser import load_client_json
from workspace_utilization_estimator.validator import validate_client_data
from workspace_utilization_estimator.reasonableness import check_reasonableness
from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.normalizer import Normalizer
from workspace_utilization_estimator.models.organization import Organization
from workspace_utilization_estimator.utilization_agent import UtilizationAgent, StubLLMClient


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

    # Phase 3 — Normalization
    try:
        client = ClientData.from_dict(data)
        normalizer = Normalizer(client)
        proxy = normalizer.to_proxy_data()

        print("✓ Normalization completed")
        print("\n--- Proxy Data (Engineered Features) ---")
        print(f"Avg Daily Presence:      {proxy.avg_daily_presence:.3f}")
        print(f"Adjusted VPN Factor:     {proxy.adjusted_vpn_factor:.3f}")
        print(f"Meeting Density Score:   {proxy.meeting_density_score:.3f}")
        print(f"Travel Absence Factor:   {proxy.travel_absence_factor:.3f}")
        print(f"Hybrid Presence Ratio:   {proxy.hybrid_presence_ratio:.3f}")
        print("----------------------------------------\n")

    except Exception as e:
        print(f"❌ Normalization failed: {e}")
        return
    
        # Phase 4 — Organization Model
    try:
        org = Organization(client, proxy)
        print("✓ Organization object created")

        print("\n--- Organization Summary ---")
        for k, v in org.summary().items():
            print(f"{k}: {v}")
        print("-----------------------------\n")

    except Exception as e:
        print(f"❌ Organization model failed: {e}")
        return

    # Phase 6 — Utilization Estimate (using stub LLM)
    try:
        agent = UtilizationAgent(StubLLMClient())
        result = agent.estimate(org)

        print("✓ Utilization estimate generated\n")
        print("--- Utilization Result ---")
        print(f"Low:          {result.low_estimate:.3f}")
        print(f"Most Likely:  {result.most_likely_estimate:.3f}")
        print(f"High:         {result.high_estimate:.3f}")
        print(f"Confidence:   {result.confidence_score:.3f}")
        print("Key Drivers:")
        for d in result.key_drivers:
            print(f"  - {d}")
        print("\nExecutive Summary:")
        print(result.executive_summary)
        print("--------------------------\n")

    except Exception as e:
        print(f"❌ Utilization agent failed: {e}")
        return


    print("\n🎉 All checks passed — input is valid and reasonable.")

if __name__ == "__main__":
    run_cli()

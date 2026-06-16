from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.models.proxy_data import ProxyData

class Organization:
    """
    Unified domain object representing a client organization.
    Holds raw client data (Phase 1), engineered proxy features (Phase 3),
    and later LLM outputs (Phase 5–6).
    """

    def __init__(self, client_data: ClientData, proxy_data: ProxyData):
        self.client_data = client_data
        self.proxy_data = proxy_data

    def summary(self) -> dict:
        """Return a structured summary for debugging or reporting."""
        return {
            "organization_name": self.client_data.organization_name,
            "employees": self.client_data.employees,
            "sqft": self.client_data.sqft,
            "proxy_features": {
                "avg_daily_presence": self.proxy_data.avg_daily_presence,
                "adjusted_vpn_factor": self.proxy_data.adjusted_vpn_factor,
                "meeting_density_score": self.proxy_data.meeting_density_score,
                "travel_absence_factor": self.proxy_data.travel_absence_factor,
                "hybrid_presence_ratio": self.proxy_data.hybrid_presence_ratio,
            }
        }

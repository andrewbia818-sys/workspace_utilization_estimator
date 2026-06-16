from workspace_utilization_estimator.models.client_data import ClientData
from workspace_utilization_estimator.models.proxy_data import ProxyData

class Normalizer:
    def __init__(self, client_data: ClientData):
        self.client = client_data

    def compute_avg_daily_presence(self):
        # Simple placeholder formula
        return (100 - self.client.travel_percentage - self.client.vpn_usage_percentage) / 100

    def compute_adjusted_vpn_factor(self):
        return self.client.vpn_usage_percentage / 100

    def compute_meeting_density_score(self):
        return min(self.client.meeting_hours / 8, 1.0)

    def compute_travel_absence_factor(self):
        return self.client.travel_percentage / 100

    def compute_hybrid_presence_ratio(self):
        return self.client.hybrid_days / 5

    def to_proxy_data(self) -> ProxyData:
        return ProxyData(
            avg_daily_presence=self.compute_avg_daily_presence(),
            adjusted_vpn_factor=self.compute_adjusted_vpn_factor(),
            meeting_density_score=self.compute_meeting_density_score(),
            travel_absence_factor=self.compute_travel_absence_factor(),
            hybrid_presence_ratio=self.compute_hybrid_presence_ratio()
        )

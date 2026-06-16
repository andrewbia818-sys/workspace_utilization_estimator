class ProxyData:
    def __init__(
        self,
        avg_daily_presence: float,
        adjusted_vpn_factor: float,
        meeting_density_score: float,
        travel_absence_factor: float,
        hybrid_presence_ratio: float
    ):
        self.avg_daily_presence = avg_daily_presence
        self.adjusted_vpn_factor = adjusted_vpn_factor
        self.meeting_density_score = meeting_density_score
        self.travel_absence_factor = travel_absence_factor
        self.hybrid_presence_ratio = hybrid_presence_ratio

class ClientData:
    def __init__(
        self,
        organization_name: str,
        employees: int,
        sqft: int,
        vacation_days: float,
        sick_days: float,
        travel_percentage: float,
        vpn_usage_percentage: float,
        peak_login_percentage: float,
        meeting_hours: float,
        hybrid_days: int
    ):
        self.organization_name = organization_name
        self.employees = employees
        self.sqft = sqft
        self.vacation_days = vacation_days
        self.sick_days = sick_days
        self.travel_percentage = travel_percentage
        self.vpn_usage_percentage = vpn_usage_percentage
        self.peak_login_percentage = peak_login_percentage
        self.meeting_hours = meeting_hours
        self.hybrid_days = hybrid_days

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

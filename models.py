from dataclasses import dataclass


@dataclass
class ProxyData:
    vacation_days: int
    sick_days: int
    travel_percentage: float
    vpn_usage_percentage: float
    peak_login_percentage: float
    meeting_hours: float
    hybrid_days: int


@dataclass
class Organization:
    name: str
    employees: int
    sqft: int
    proxy_data: ProxyData

@dataclass
class UtilizationEstimate:
    low: float
    most_likely: float
    high: float
    confidence: float
    patterns: list[str]
    executive_interpretation: str
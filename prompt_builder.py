from workspace_utilization_estimator.models.organization import Organization

class PromptBuilder:
    """
    Builds a structured, unambiguous prompt for the LLM using the Organization model.
    Includes explicit unit definitions for all client inputs and engineered features.
    """

    def __init__(self, organization: Organization):
        self.org = organization

    def build_prompt(self) -> str:
        client = self.org.client_data
        proxy = self.org.proxy_data

        prompt = f"""
You are an expert in workplace utilization analytics. 
Analyze the following organization using the provided raw inputs and engineered proxy features.

### Definitions (Raw Client Inputs)
- Vacation Days: number of paid vacation days per employee per year.
- Sick Days: number of sick days per employee per year.
- Meeting Hours: average number of meeting hours per employee per workday.
- Hybrid Days: number of days per week employees may work remotely (0–5).
- Travel Percentage: percent of employees traveling on any given day.
- VPN Usage Percentage: percent of employees working remotely via VPN.
- Peak Login Percentage: percent of employees logged in during peak hours.
- Square Footage: total usable office square footage.

### Definitions (Engineered Proxy Features)
- Avg Daily Presence: estimated percent of employees physically present on a typical day.
- Adjusted VPN Factor: normalized remote‑work intensity (VPN usage ÷ 100).
- Meeting Density Score: meeting load relative to an 8‑hour workday.
- Travel Absence Factor: normalized travel‑related absence (travel percentage ÷ 100).
- Hybrid Presence Ratio: hybrid days divided by 5.

### Raw Client Data
- Organization Name: {client.organization_name}
- Employees: {client.employees}
- Square Footage: {client.sqft}
- Vacation Days (per year): {client.vacation_days}
- Sick Days (per year): {client.sick_days}
- Travel Percentage: {client.travel_percentage}
- VPN Usage Percentage: {client.vpn_usage_percentage}
- Peak Login Percentage: {client.peak_login_percentage}
- Meeting Hours (per workday): {client.meeting_hours}
- Hybrid Days (per week): {client.hybrid_days}

### Engineered Proxy Features
- Avg Daily Presence: {proxy.avg_daily_presence:.3f}
- Adjusted VPN Factor: {proxy.adjusted_vpn_factor:.3f}
- Meeting Density Score: {proxy.meeting_density_score:.3f}
- Travel Absence Factor: {proxy.travel_absence_factor:.3f}
- Hybrid Presence Ratio: {proxy.hybrid_presence_ratio:.3f}

### Task
Using the definitions above, estimate the organization's workspace utilization using the following JSON structure:

{{
  "low_estimate": <float>,
  "most_likely_estimate": <float>,
  "high_estimate": <float>,
  "confidence_score": <float between 0 and 1>,
  "key_drivers": [
      "string explaining factor 1",
      "string explaining factor 2"
  ],
  "executive_summary": "A concise narrative explaining the utilization estimate."
}}

Respond ONLY with valid JSON.
"""
        return prompt.strip()


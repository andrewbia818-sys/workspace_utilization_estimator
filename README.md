# Workspace Utilization Estimator

A Python-based backend application that estimates office space utilization using indirect indicators such as hybrid work policies, employee absences, travel patterns, VPN usage, and meeting behavior.

The project uses a Large Language Model (LLM) to analyze organizational data and produce utilization estimates, confidence scores, and explanatory insights that can support workplace planning and real estate decision-making.

This project was developed as part of my Backend Development studies through Boot.dev and serves as the first building block of a larger AI-assisted Facilities and Real Estate Advisory platform.

---

## Background

Organizations often know which workspaces are assigned to employees, but frequently lack reliable information about how those spaces are actually used throughout the day.

Traditional utilization studies typically require:

* Physical occupancy sensors
* Manual observation studies
* Badge access monitoring
* Dedicated consulting engagements

These approaches can be costly, intrusive, and difficult to implement.

The goal of this project is to explore whether useful occupancy estimates can be generated using non-intrusive proxy data that many organizations already possess.

Examples include:

* Employee leave statistics
* Business travel data
* Hybrid work policies
* VPN usage patterns
* Office login activity
* Meeting schedules

The output is intended to be directional and decision-supportive rather than a substitute for detailed occupancy measurement.

Normalization of Client Data

A further complication in this sort of analysis is that an organization may not have direct access to the proxy data required. A further refinement of this project will be to refine the normalization process that converts input data from the client to the set of proxy data. This will be an additional layer in the overall architecture of the solution but is out of scope of this project.

---

## Features

* Validates organizational input data
* Calculates basic workplace metrics
* Uses Google's Gemini API to estimate workspace utilization
* Produces:

  * Low-case utilization estimate
  * Most-likely utilization estimate
  * High-case utilization estimate
  * Confidence score
  * Key utilization patterns
  * Executive interpretation
* Outputs structured JSON results
* Command-line interface

---

## Example Input

```json
{
  "employees": 480,
  "sqft": 120000,
  "vacation_days": 18,
  "sick_days": 6,
  "travel_percentage": 10,
  "vpn_usage_percentage": 35,
  "peak_login_percentage": 65,
  "meeting_hours": 3.5,
  "hybrid_days": 3
}
```

---

## Example Output

```json
{
  "utilization": {
    "low": 0.45,
    "most_likely": 0.58,
    "high": 0.72
  },
  "confidence": 0.69,
  "patterns": [
    "Midweek occupancy peaks",
    "Monday and Friday underutilization",
    "Meeting-heavy culture reduces desk utilization"
  ],
  "executive_interpretation": "The organization appears materially over-provisioned relative to probable occupancy patterns."
}
```
## Units
```
| Field | Meaning | Units |
| --- | --- | --- |
| ``organization_name`` | Name of the organization | string |
| ``employees`` | Total number of employees | count |
| ``sqft`` | Total usable office square footage | square feet |
| ``vacation_days`` | Paid vacation days per employee per year | days/year |
| ``sick_days`` | Sick days per employee per year | days/year |
| ``travel_percentage`` | Percent of employees traveling on a typical day | % (0–100) |
| ``vpn_usage_percentage`` | Percent of employees working remotely via VPN | % (0–100) |
| ``peak_login_percentage`` | Percent of employees logged in during peak hours | % (0–100) |
| ``meeting_hours`` | Average meeting hours per employee per workday | hours/day |
| ``hybrid_days`` | Number of days per week employees may work remotely | days/week (0–5) |
```
## Proxy Formulas

| Proxy Feature | Formula | Meaning |
| --- | --- | --- |
| ``avg_daily_presence`` | ``(100 ``- ``travel_percentage ``- ``vpn_usage_percentage) ``/ ``100`` | Estimated percent of employees physically present on a typical day |
| ``adjusted_vpn_factor`` | ``vpn_usage_percentage ``/ ``100`` | Normalized remote‑work intensity |
| ``meeting_density_score`` | ``meeting_hours ``/ ``8`` (capped at 1.0) | Meeting load relative to an 8‑hour day |
| ``travel_absence_factor`` | ``travel_percentage ``/ ``100`` | Normalized travel‑related absence |
| ``hybrid_presence_ratio`` | ``hybrid_days ``/ ``5`` | Hybrid schedule intensity |

---

## Technology Stack

* Python 3
* Google Gemini API
* JSON
* Object-Oriented Programming
* Unit Testing
* Git and GitHub

Planned future technologies include:

* FastAPI
* PostgreSQL
* ReportLab
* python-pptx
* Streamlit

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/workspace-utilization-estimator.git
```

Navigate to the project directory:

```bash
cd workspace-utilization-estimator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your Gemini API key:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

Run the application:

```bash
python3 main.py sample_input.json
```

---

## Project Structure

```text
workspace-utilization-estimator/

├── main.py
├── models.py
├── validator.py
├── normalizer.py
├── prompt_builder.py
├── utilization_agent.py
├── parser.py
├── config.py
├── data/
├── outputs/
└── tests/
```

---

## Learning Objectives

This project was built to practice:

* Backend software design
* API integration
* Object-oriented programming
* Data validation
* Prompt engineering
* JSON processing
* Error handling
* Automated testing
* Git and GitHub workflows

---

## Future Enhancements

Planned improvements include:

### Phase 2

* Client input data normalization
* Financial impact modeling
* Scenario analysis
* Savings estimates

### Phase 3

* Automated report generation
* PowerPoint slide generation
* PDF export

### Phase 4

* Web-based interface
* Multi-client support
* Historical trend analysis

### Phase 5

* Complete AI-assisted Facilities Advisory Platform

---

## Disclaimer

The utilization estimates produced by this software are based on indirect indicators and AI-assisted inference. Results should be considered decision-support information rather than precise occupancy measurements.

Where major real estate or workplace transformation decisions are contemplated, additional analysis and validation may be appropriate.

---

## Author

Andrew Nye

Former Chief of Facilities Management, United Nations Headquarters

BSc Electrical & Electronic Engineer (University of Nottingham)

MBA (Open University)
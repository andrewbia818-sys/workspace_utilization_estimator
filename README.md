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
python main.py sample_input.json
```

---

## Project Structure

```text
workspace-utilization-estimator/

├── main.py
├── models.py
├── validator.py
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

Electrical & Electronic Engineer (University of Nottingham)

MBA (Open University)

Former Chief of Facilities Management, United Nations Headquarters

Personal Finance Blog:
https://badinvestmentsadvice.com

United Nations Retirees Association Website:
http://www.aficsny.org

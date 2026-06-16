def check_reasonableness(data: dict) -> None:
    errors = []

    # Employees and sqft must be positive
    if data["employees"] <= 0:
        errors.append("Employees must be greater than zero.")

    if data["sqft"] <= 0:
        errors.append("Square footage must be greater than zero.")

    # Basic sanity: sqft per employee
    sqft_per_employee = data["sqft"] / data["employees"]
    if sqft_per_employee < 50:
        errors.append("Square footage per employee is unrealistically low (< 50 sqft).")
    if sqft_per_employee > 1000:
        errors.append("Square footage per employee is unrealistically high (> 1000 sqft).")

    # Hybrid days must be <= 5 for most orgs
    if data["hybrid_days"] > 5:
        errors.append("Hybrid days > 5 is unusual and may indicate incorrect input.")

    # Meeting hours sanity
    if data["meeting_hours"] > 10:
        errors.append("Meeting hours > 10 per day is unrealistic.")

    # Travel percentage sanity
    if data["travel_percentage"] > 50:
        errors.append("Travel percentage > 50% is unlikely for most organizations.")

    if errors:
        raise ValueError("Reasonableness check failed: " + "; ".join(errors))

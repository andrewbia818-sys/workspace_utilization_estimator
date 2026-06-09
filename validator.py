def validate_organization(org: Organization):

    if not org.name:
        raise ValueError("name must be non-empty")
    
    if org.employees <= 0:
        raise ValueError("employees must be positive")

    if org.sqft <= 0:
        raise ValueError("sqft must be positive")

    if not 0 <= org.proxy_data.travel_percentage <= 100:
        raise ValueError("travel percentage invalid")

    if not 0 <= org.proxy_data.hybrid_days <= 7:
        raise ValueError("hybrid days must be between 0 and 7")
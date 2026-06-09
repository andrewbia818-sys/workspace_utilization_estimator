def load_organization(path):
    with open(path, 'r') as f:
        data = json.load(f)
    
    proxy_data = ProxyData(**data['proxy_data'])
    org = Organization(
        name=data['name'],
        employees=data['employees'],
        sqft=data['sqft'],
        proxy_data=proxy_data
    )
    return org
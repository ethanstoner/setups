# API Client Template

A reusable REST API client with rate limiting, retries, and error handling.

## Features

- Rate limiting to respect API limits
- Automatic retries with exponential backoff
- Request/response logging
- Error handling
- Easy to extend for any API

## Usage

```python
from api_client import APIClient

# Create client
client = APIClient(
    base_url="https://api.example.com",
    api_key="your_api_key",
    rate_limit=60  # requests per minute
)

# Make requests
response = client.get("/endpoint")
data = client.post("/endpoint", json={"key": "value"})
```

## Customization

Extend the `APIClient` class for API-specific methods:

```python
class MyAPIClient(APIClient):
    def get_user(self, user_id):
        return self.get(f"/users/{user_id}")
    
    def create_user(self, data):
        return self.post("/users", json=data)
```


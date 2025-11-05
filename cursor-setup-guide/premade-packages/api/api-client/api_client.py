#!/usr/bin/env python3
"""
API Client Template
Reusable REST API client with rate limiting, retries, and error handling.
"""

import requests
import time
from typing import Optional, Dict, Any
from datetime import datetime, timedelta
from collections import deque


class RateLimiter:
    """Simple rate limiter using token bucket algorithm."""
    
    def __init__(self, max_requests: int, period: float = 60.0):
        """
        Args:
            max_requests (int): Maximum requests allowed
            period (float): Time period in seconds
        """
        self.max_requests = max_requests
        self.period = period
        self.requests = deque()
    
    def wait_if_needed(self):
        """Wait if rate limit would be exceeded."""
        now = time.time()
        
        # Remove old requests outside the period
        while self.requests and self.requests[0] < now - self.period:
            self.requests.popleft()
        
        # If at limit, wait until oldest request expires
        if len(self.requests) >= self.max_requests:
            sleep_time = self.requests[0] + self.period - now
            if sleep_time > 0:
                time.sleep(sleep_time)
        
        self.requests.append(time.time())


class APIClient:
    """REST API client with rate limiting and retries."""
    
    def __init__(
        self,
        base_url: str,
        api_key: Optional[str] = None,
        rate_limit: int = 60,
        rate_period: float = 60.0,
        max_retries: int = 3,
        retry_delay: float = 1.0,
        timeout: float = 10.0
    ):
        """
        Args:
            base_url (str): Base API URL
            api_key (str, optional): API key for authentication
            rate_limit (int): Requests per period
            rate_period (float): Rate limit period in seconds
            max_retries (int): Maximum retry attempts
            retry_delay (float): Initial retry delay in seconds
            timeout (float): Request timeout in seconds
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.rate_limiter = RateLimiter(rate_limit, rate_period)
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.timeout = timeout
        
        # Default headers
        self.headers = {
            "Content-Type": "application/json",
            "User-Agent": "APIClient/1.0"
        }
        
        if api_key:
            self.headers["Authorization"] = f"Bearer {api_key}"
    
    def _make_request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> Optional[requests.Response]:
        """
        Make HTTP request with rate limiting and retries.
        
        Args:
            method (str): HTTP method
            endpoint (str): API endpoint
            **kwargs: Additional arguments for requests
        
        Returns:
            requests.Response or None
        """
        url = f"{self.base_url}{endpoint}"
        
        # Merge headers
        headers = {**self.headers, **kwargs.pop('headers', {})}
        
        for attempt in range(self.max_retries + 1):
            try:
                # Rate limiting
                self.rate_limiter.wait_if_needed()
                
                # Make request
                response = requests.request(
                    method,
                    url,
                    headers=headers,
                    timeout=self.timeout,
                    **kwargs
                )
                
                # Check for rate limit errors
                if response.status_code == 429:
                    retry_after = int(response.headers.get('Retry-After', self.retry_delay))
                    if attempt < self.max_retries:
                        print(f"Rate limited. Waiting {retry_after}s...")
                        time.sleep(retry_after)
                        continue
                
                # Raise for other errors
                response.raise_for_status()
                return response
                
            except requests.exceptions.RequestException as e:
                if attempt < self.max_retries:
                    delay = self.retry_delay * (2 ** attempt)  # Exponential backoff
                    print(f"Request failed, retrying in {delay}s... ({attempt + 1}/{self.max_retries})")
                    time.sleep(delay)
                else:
                    print(f"Request failed after {self.max_retries} attempts: {e}")
                    return None
        
        return None
    
    def get(self, endpoint: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """GET request."""
        response = self._make_request("GET", endpoint, **kwargs)
        return response.json() if response else None
    
    def post(self, endpoint: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """POST request."""
        response = self._make_request("POST", endpoint, **kwargs)
        return response.json() if response else None
    
    def put(self, endpoint: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """PUT request."""
        response = self._make_request("PUT", endpoint, **kwargs)
        return response.json() if response else None
    
    def delete(self, endpoint: str, **kwargs) -> Optional[Dict[Any, Any]]:
        """DELETE request."""
        response = self._make_request("DELETE", endpoint, **kwargs)
        return response.json() if response else None


if __name__ == "__main__":
    # Example usage
    client = APIClient(
        base_url="https://api.example.com",
        api_key="your_api_key",
        rate_limit=60
    )
    
    data = client.get("/endpoint")
    print(data)


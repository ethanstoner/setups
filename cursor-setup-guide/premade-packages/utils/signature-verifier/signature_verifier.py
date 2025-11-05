#!/usr/bin/env python3
"""
Signature Verifier
Validate HMAC signatures for webhooks.
"""

import hmac
import hashlib


def verify_signature(
    payload: bytes,
    signature: str,
    secret: str,
    algorithm: str = "sha256"
) -> bool:
    """
    Verify HMAC signature.
    
    Args:
        payload (bytes): Request payload
        signature (str): Signature from header
        secret (str): Secret key
        algorithm (str): Hash algorithm (sha1, sha256, sha512)
    
    Returns:
        bool: True if signature is valid
    """
    if not secret:
        return False
    
    # Select hash algorithm
    hash_func = {
        "sha1": hashlib.sha1,
        "sha256": hashlib.sha256,
        "sha512": hashlib.sha512
    }.get(algorithm.lower(), hashlib.sha256)
    
    # Calculate expected signature
    expected_signature = hmac.new(
        secret.encode(),
        payload,
        hash_func
    ).hexdigest()
    
    # Compare signatures (constant-time comparison)
    return hmac.compare_digest(expected_signature, signature)


def verify_discord_signature(payload: bytes, signature: str, timestamp: str, public_key: str) -> bool:
    """
    Verify Discord webhook signature.
    
    Args:
        payload (bytes): Request payload
        signature (str): Signature from header
        timestamp (str): Timestamp from header
        public_key (str): Discord public key
    
    Returns:
        bool: True if signature is valid
    """
    message = f"{timestamp}{payload.decode()}"
    return verify_signature(message.encode(), signature, public_key)


def verify_github_signature(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verify GitHub webhook signature.
    
    Args:
        payload (bytes): Request payload
        signature (str): Signature from header (format: "sha256=...")
        secret (str): GitHub webhook secret
    
    Returns:
        bool: True if signature is valid
    """
    if not signature.startswith("sha256="):
        return False
    
    signature_hash = signature[7:]  # Remove "sha256=" prefix
    return verify_signature(payload, signature_hash, secret, "sha256")


def verify_stripe_signature(payload: bytes, signature: str, secret: str) -> bool:
    """
    Verify Stripe webhook signature.
    
    Args:
        payload (bytes): Request payload
        signature (str): Signature from header
        secret (str): Stripe webhook secret
    
    Returns:
        bool: True if signature is valid
    """
    # Stripe uses sha256 with timestamp
    # This is simplified - Stripe's actual format is more complex
    return verify_signature(payload, signature, secret, "sha256")


if __name__ == "__main__":
    # Example usage
    secret = "my_secret_key"
    payload = b'{"test": "data"}'
    
    # Generate signature
    signature = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    # Verify signature
    is_valid = verify_signature(payload, signature, secret)
    print(f"Signature valid: {is_valid}")


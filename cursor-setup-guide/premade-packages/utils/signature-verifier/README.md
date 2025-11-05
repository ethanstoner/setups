# Signature Verifier

Template for validating HMAC signatures on incoming webhooks (Discord, Stripe, GitHub).

## Features

- HMAC signature verification
- Support for multiple algorithms
- Easy to integrate with webhook handlers

## Usage

```python
from signature_verifier import verify_signature

# Verify signature
is_valid = verify_signature(
    payload=request_body,
    signature=request.headers.get('X-Signature'),
    secret="your_secret_key"
)

if not is_valid:
    return "Invalid signature", 401
```

## Supported Providers

- Discord webhooks
- GitHub webhooks
- Stripe webhooks
- Custom HMAC signatures


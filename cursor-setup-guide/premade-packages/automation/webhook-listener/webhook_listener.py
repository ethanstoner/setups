#!/usr/bin/env python3
"""
Webhook Listener Server
Receives and logs incoming webhooks with optional signature verification.
"""

from flask import Flask, request, jsonify
import json
import os
import hmac
import hashlib
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "")
LOG_DIR = Path("webhook_logs")
LOG_DIR.mkdir(exist_ok=True)


def verify_signature(payload, signature, secret):
    """
    Verify webhook signature using HMAC.
    
    Args:
        payload (bytes): Request payload
        signature (str): Signature from header
        secret (str): Secret key
    
    Returns:
        bool: True if signature is valid
    """
    if not secret:
        return True  # Skip verification if no secret set
    
    expected_signature = hmac.new(
        secret.encode(),
        payload,
        hashlib.sha256
    ).hexdigest()
    
    return hmac.compare_digest(expected_signature, signature)


@app.route('/webhook', methods=['POST'])
def webhook():
    """Handle incoming webhook."""
    try:
        # Get raw payload for signature verification
        payload = request.get_data()
        
        # Get signature from header (adjust header name as needed)
        signature = request.headers.get('X-Signature', '')
        
        # Verify signature if secret is set
        if WEBHOOK_SECRET and not verify_signature(payload, signature, WEBHOOK_SECRET):
            return jsonify({"error": "Invalid signature"}), 401
        
        # Parse JSON payload
        data = request.get_json() or {}
        
        # Log the webhook
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        log_file = LOG_DIR / f"webhook_{timestamp}.json"
        
        log_data = {
            "timestamp": datetime.now().isoformat(),
            "headers": dict(request.headers),
            "payload": data,
            "ip": request.remote_addr
        }
        
        with open(log_file, 'w') as f:
            json.dump(log_data, f, indent=2)
        
        print(f"Webhook received: {log_file}")
        
        # Add your custom handling here
        # For example, forward to Discord, process data, etc.
        
        return jsonify({"status": "received", "logged": True}), 200
        
    except Exception as e:
        print(f"Error processing webhook: {e}")
        return jsonify({"error": str(e)}), 500


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"}), 200


if __name__ == '__main__':
    print(f"Webhook listener starting on http://localhost:5000/webhook")
    print(f"Logs will be saved to: {LOG_DIR}")
    if WEBHOOK_SECRET:
        print("Signature verification: ENABLED")
    else:
        print("Signature verification: DISABLED (set WEBHOOK_SECRET in .env)")
    
    app.run(host='0.0.0.0', port=5000, debug=True)


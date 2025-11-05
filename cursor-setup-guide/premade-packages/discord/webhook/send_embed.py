#!/usr/bin/env python3
"""
Discord Webhook Embed Sender
Send rich embeds to Discord using webhooks.
"""

import requests
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not WEBHOOK_URL:
    print("Error: WEBHOOK_URL not found in environment variables")
    exit(1)


def send_webhook_embed(title, description, color=0x00ff00, fields=None, footer=None):
    """
    Send an embed message via Discord webhook.
    
    Args:
        title (str): Embed title
        description (str): Embed description
        color (int): Embed color (hex color code)
        fields (list, optional): List of dicts with 'name' and 'value' keys
        footer (str, optional): Footer text
    
    Returns:
        bool: True if successful, False otherwise
    """
    embed = {
        "title": title,
        "description": description,
        "color": color,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    if fields:
        embed["fields"] = fields
    
    if footer:
        embed["footer"] = {"text": footer}
    
    payload = {
        "embeds": [embed]
    }
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        
        if response.status_code == 204:
            print("Embed sent successfully!")
            return True
        else:
            print(f"Failed to send embed. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    # Example: Send an embed with fields
    fields = [
        {"name": "Field 1", "value": "Value 1", "inline": True},
        {"name": "Field 2", "value": "Value 2", "inline": True},
        {"name": "Field 3", "value": "Value 3", "inline": False}
    ]
    
    send_webhook_embed(
        title="Example Embed",
        description="This is an example embed message",
        color=0x3498db,  # Blue color
        fields=fields,
        footer="Sent via webhook"
    )


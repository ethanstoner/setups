#!/usr/bin/env python3
"""
Discord Webhook Sender
Send messages to Discord using webhooks.
"""

import requests
import json
import os
import sys
import argparse
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

WEBHOOK_URL = os.getenv("WEBHOOK_URL")

if not WEBHOOK_URL:
    print("Error: WEBHOOK_URL not found in environment variables")
    print("Create a .env file with: WEBHOOK_URL=your_webhook_url_here")
    sys.exit(1)


def send_webhook_message(content, username=None, avatar_url=None):
    """
    Send a message via Discord webhook.
    
    Args:
        content (str): Message content
        username (str, optional): Custom username for webhook
        avatar_url (str, optional): Custom avatar URL for webhook
    
    Returns:
        bool: True if successful, False otherwise
    """
    payload = {
        "content": content
    }
    
    if username:
        payload["username"] = username
    
    if avatar_url:
        payload["avatar_url"] = avatar_url
    
    try:
        response = requests.post(WEBHOOK_URL, json=payload)
        
        if response.status_code == 204:
            print("Message sent successfully!")
            return True
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send message to Discord via webhook")
    parser.add_argument("message", help="Message to send")
    parser.add_argument("--username", "-u", help="Custom username")
    parser.add_argument("--avatar", "-a", help="Custom avatar URL")
    
    args = parser.parse_args()
    
    send_webhook_message(args.message, args.username, args.avatar)


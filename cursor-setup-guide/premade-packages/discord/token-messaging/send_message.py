#!/usr/bin/env python3
"""
Discord Token Messaging
Send messages to Discord channels using your Discord account token.
"""

import requests
import json
import os
import sys
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = os.getenv("CHANNEL_ID")

if not DISCORD_TOKEN:
    print("Error: DISCORD_TOKEN not found in environment variables")
    print("Create a .env file with: DISCORD_TOKEN=your_token_here")
    sys.exit(1)

if not CHANNEL_ID:
    print("Error: CHANNEL_ID not found in environment variables")
    print("Create a .env file with: CHANNEL_ID=your_channel_id_here")
    sys.exit(1)


def send_discord_message(message_content, channel_id=None):
    """
    Send a message to a Discord channel using the Discord API.
    
    Args:
        message_content (str): The message to send
        channel_id (str, optional): Channel ID. Uses default if not provided.
    
    Returns:
        bool: True if successful, False otherwise
    """
    if channel_id is None:
        channel_id = CHANNEL_ID
    
    api_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    
    headers = {
        "Authorization": DISCORD_TOKEN,
        "Content-Type": "application/json"
    }
    
    payload = {
        "content": message_content
    }
    
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print("Message sent successfully!")
            return True
        else:
            print(f"Failed to send message. Status code: {response.status_code}")
            print(f"Response: {response.json()}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        message = " ".join(sys.argv[1:])
        send_discord_message(message)
    else:
        print("Usage: python send_message.py 'Your message here'")
        print("Or set MESSAGE environment variable")


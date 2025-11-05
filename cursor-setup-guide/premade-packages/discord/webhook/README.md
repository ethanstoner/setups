# Discord Webhook

Send messages to Discord channels using webhooks (no token required).

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a Discord Webhook:
   - Go to your Discord server
   - Go to Server Settings → Integrations → Webhooks
   - Click "New Webhook"
   - Give it a name and select a channel
   - Click "Copy Webhook URL"
   - Save the URL

3. Create `.env` file:
```env
WEBHOOK_URL=https://discord.com/api/webhooks/your_webhook_url_here
```

## Usage

```bash
# Send a simple message
python send_webhook.py "Hello from webhook!"

# Send with username and avatar
python send_webhook.py "Hello!" --username "My Bot" --avatar "https://example.com/avatar.png"

# Send an embed
python send_embed.py
```

## Advantages

- No bot token needed
- No authentication required
- Easy to set up
- Perfect for notifications and simple messaging

## Limitations

- Cannot read messages
- Cannot respond to commands
- Limited to sending messages only


# Webhook Listener

A ready-to-use webhook listener server using Flask that logs incoming webhooks and optionally verifies signatures.

## Features

- Receives and logs webhook payloads
- Optional signature verification (HMAC)
- Saves payloads to JSON files
- Easy to extend for custom webhook handling

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python webhook_listener.py
```

The server will start on `http://localhost:5000/webhook`

## Usage

### Test with curl

```bash
curl -X POST http://localhost:5000/webhook \
  -H "Content-Type: application/json" \
  -d '{"test": "data"}'
```

### Configure for Discord Webhooks

Set `DISCORD_WEBHOOK_SECRET` in `.env` for signature verification.

### View Logs

Check the `webhook_logs/` directory for saved payloads.

## Customization

Edit `webhook_listener.py` to add custom handling logic for your specific webhook provider.


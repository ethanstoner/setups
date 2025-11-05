# Discord Token Messaging

Send messages to Discord channels using your Discord account token.

## Setup

1. Install dependencies:
```bash
pip install requests
```

2. Get your Discord token:
   - Open Discord in your browser
   - Press `F12` to open Developer Tools
   - Go to Network tab
   - Send a message in any channel
   - Find the request to `messages` endpoint
   - Look for `Authorization` header - that's your token

3. Get Channel ID:
   - Enable Developer Mode in Discord (Settings → Advanced → Developer Mode)
   - Right-click on the channel
   - Click "Copy ID"

4. Create a `.env` file:
```env
DISCORD_TOKEN=your_token_here
CHANNEL_ID=your_channel_id_here
```

## Usage

```bash
python send_message.py "Hello from Python!"
```

## Security Warning

Never commit your Discord token to version control. Always use environment variables or a `.env` file (which should be in `.gitignore`).


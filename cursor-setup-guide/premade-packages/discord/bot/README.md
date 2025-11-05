# Discord Bot

A simple Discord bot using discord.py library.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a Discord Bot:
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application"
   - Give it a name
   - Go to "Bot" section
   - Click "Add Bot"
   - Copy the bot token
   - Enable "Message Content Intent" under "Privileged Gateway Intents"

3. Invite bot to server:
   - Go to "OAuth2" → "URL Generator"
   - Select "bot" scope
   - Select permissions (Send Messages, Read Message History)
   - Copy the URL and open it in browser
   - Select your server and authorize

4. Create `.env` file:
```env
DISCORD_BOT_TOKEN=your_bot_token_here
```

## Usage

```bash
python bot.py
```

## Features

This example bot includes:
- Responds to !hello command
- Responds to !ping command
- Logs messages to console
- Error handling

## Customization

Edit `bot.py` to add your own commands and features.


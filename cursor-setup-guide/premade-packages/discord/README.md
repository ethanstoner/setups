# Discord Packages

Complete Discord integration packages for various use cases.

## Available Packages

1. **[Token Messaging](./token-messaging/)**
   - Send messages using your Discord account token
   - Simple API-based messaging
   - No bot setup required
   - Perfect for personal automation

2. **[Discord Bot](./bot/)**
   - Full Discord bot using discord.py
   - Command handling (!hello, !ping, !info)
   - Event system
   - Perfect for interactive bots
   - Requires bot token from Discord Developer Portal

3. **[Webhook](./webhook/)**
   - Send messages via webhooks
   - No authentication needed
   - Great for notifications and alerts
   - Support for embeds and rich formatting
   - Easiest to set up

## Which One Should I Use?

- **Token Messaging**: For personal automation using your account
- **Discord Bot**: For interactive bots with commands and responses
- **Webhook**: For simple notifications and one-way messaging

## Quick Start

1. Choose the package that fits your needs
2. Navigate to the folder
3. Read the `README.md` for setup instructions
4. Copy `.env.example` to `.env` and fill in your credentials
5. Install dependencies: `pip install -r requirements.txt`
6. Copy the package to your project or run directly!

## Security

- Never commit `.env` files to version control
- Keep your tokens and webhook URLs secure
- Use environment variables for production deployments


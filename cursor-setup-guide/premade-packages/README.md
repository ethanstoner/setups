# Premade Packages

Ready-to-use code packages for common development tasks. Simply copy the package to your project and customize as needed.

## Available Packages

### Discord Integration

All Discord packages are organized in the [`discord/`](./discord/) folder:

- **[Token Messaging](./discord/token-messaging/)** - Send messages using your Discord account token
- **[Discord Bot](./discord/bot/)** - Full Discord bot with commands and events
- **[Webhook](./discord/webhook/)** - Send messages via webhooks (easiest setup)

See the [Discord README](./discord/README.md) for detailed information about each package.

### Automation

- **[Webhook Listener](./automation/webhook-listener/)** - Receive and log webhooks with Flask
- **[Email Sender](./automation/email-sender/)** - Send templated HTML emails via SMTP
- **[File Watcher](./automation/file-watcher/)** - Monitor directory for file changes

### API Tools

- **[API Client](./api/api-client/)** - Reusable REST API client with rate limiting and retries

### Database

- **[SQLite Connector](./database/sqlite-connector/)** - SQLAlchemy setup with example CRUD operations

### Utilities

- **[Logger](./utils/logger/)** - Structured logging with console and file output
- **[Environment Manager](./utils/env-manager/)** - Check and generate .env files
- **[Signature Verifier](./utils/signature-verifier/)** - Validate HMAC signatures for webhooks

### Development Tools

- **[CLI Menu](./dev-tools/cli-menu/)** - Interactive command-line menu system
- **[Config Manager](./dev-tools/config-manager/)** - Handle YAML/JSON configuration files

### Server Development

**[Localhost Server](./localhost-server/)**
   - Python HTTP server tutorial
   - Auto-browser opening
   - Port conflict handling
   - Example HTML page

## Quick Start

Each package folder contains:
- `README.md` - Setup instructions
- Working code files
- `requirements.txt` - Python dependencies
- `.env.example` - Environment variable template
- `.gitignore` - Git ignore rules

## Usage

1. Navigate to the package folder
2. Read the `README.md` for setup instructions
3. Copy `.env.example` to `.env` and fill in your credentials
4. Install dependencies: `pip install -r requirements.txt`
5. Copy the package code to your project or run directly!

## Security

Always use `.env` files for sensitive information like tokens and API keys. Never commit `.env` files to version control.

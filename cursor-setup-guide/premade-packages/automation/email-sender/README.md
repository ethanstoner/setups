# Email Sender

Send templated HTML emails using Gmail API or SMTP.

## Features

- Send HTML emails with template variables
- Support for Gmail API and SMTP
- Attachment support
- Template system with placeholders

## Setup

### Option 1: Gmail API

1. Enable Gmail API in Google Cloud Console
2. Create credentials and download `credentials.json`
3. Set `GMAIL_CREDENTIALS_PATH` in `.env`

### Option 2: SMTP

1. Set SMTP credentials in `.env`:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

## Usage

```python
from email_sender import send_email

# Send simple email
send_email(
    to="recipient@example.com",
    subject="Hello",
    body="This is a test email"
)

# Send templated email
send_email(
    to="recipient@example.com",
    subject="Welcome {{name}}!",
    body="Your code is: {{code}}",
    template_vars={"name": "John", "code": "12345"}
)
```

## Security

- Never commit credentials to version control
- Use app passwords for Gmail (not your main password)
- Store credentials in `.env` file


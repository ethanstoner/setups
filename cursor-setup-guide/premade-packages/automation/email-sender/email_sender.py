#!/usr/bin/env python3
"""
Email Sender
Send templated HTML emails using Gmail API or SMTP.
"""

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import Optional, Dict, List
from dotenv import load_dotenv

load_dotenv()


def render_template(template: str, variables: Dict[str, str]) -> str:
    """
    Render template with variables.
    
    Args:
        template (str): Template string with {{variable}} placeholders
        variables (dict): Variables to replace
    
    Returns:
        str: Rendered template
    """
    result = template
    for key, value in variables.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))
    return result


def send_email_smtp(
    to: str,
    subject: str,
    body: str,
    html: bool = False,
    from_email: Optional[str] = None,
    attachments: Optional[List[str]] = None,
    template_vars: Optional[Dict[str, str]] = None
) -> bool:
    """
    Send email using SMTP.
    
    Args:
        to (str): Recipient email
        subject (str): Email subject
        body (str): Email body
        html (bool): Whether body is HTML
        from_email (str, optional): Sender email
        attachments (list, optional): List of file paths to attach
        template_vars (dict, optional): Variables to replace in template
    
    Returns:
        bool: True if successful
    """
    smtp_host = os.getenv("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")
    
    if not smtp_user or not smtp_password:
        print("Error: SMTP_USER and SMTP_PASSWORD must be set in .env")
        return False
    
    if not from_email:
        from_email = smtp_user
    
    # Render template if variables provided
    if template_vars:
        subject = render_template(subject, template_vars)
        body = render_template(body, template_vars)
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    
    # Add body
    msg.attach(MIMEText(body, 'html' if html else 'plain'))
    
    # Add attachments
    if attachments:
        for file_path in attachments:
            if os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        'Content-Disposition',
                        f'attachment; filename={os.path.basename(file_path)}'
                    )
                    msg.attach(part)
    
    try:
        # Send email
        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()
        
        print(f"Email sent successfully to {to}")
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


def send_email(
    to: str,
    subject: str,
    body: str,
    html: bool = False,
    from_email: Optional[str] = None,
    attachments: Optional[List[str]] = None,
    template_vars: Optional[Dict[str, str]] = None
) -> bool:
    """
    Send email (wrapper function).
    
    Currently uses SMTP. Can be extended to support Gmail API.
    """
    return send_email_smtp(
        to=to,
        subject=subject,
        body=body,
        html=html,
        from_email=from_email,
        attachments=attachments,
        template_vars=template_vars
    )


if __name__ == "__main__":
    # Example usage
    send_email(
        to="recipient@example.com",
        subject="Test Email",
        body="This is a test email from Python!",
        template_vars={"name": "Test User"}
    )


import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(subject, body):
    sender_email = os.getenv("DEV_EMAIL")
    sender_name = 'Notification Bot'
    password = os.getenv("DEV_EMAIL_PWD")
    recipient = os.getenv("PERSONAL_EMAIL")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = formataddr((sender_name, sender_email))
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
        logging.info("Email sent successfully.")
    except smtplib.SMTPAuthenticationError:
        logging.error("Authentication failed. Check your email credentials.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP error occurred. Details: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred while sending email. Details: {e}")

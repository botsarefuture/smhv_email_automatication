import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_custom_email(smtp: dict, recipient_name: str, recipient_email: str, event_info: dict):
    """
    Send a custom email to remind recipients about an event.

    Args:
        smtp (dict): A dictionary containing SMTP server configuration.
            - server (str): The SMTP server address.
            - port (int, optional): The SMTP server port (default is 587).
            - email (str): The sender's email address.
            - password (str): The sender's email password.
        recipient_name (str): The recipient's name.
        recipient_email (str): The recipient's email address.
        event_info (dict): A dictionary containing event details.
            - event_name (str): The name of the event.
            - event_date (str): The date of the event.
            - event_location (str): The location of the event.

    Raises:
        Exception: If there is an error sending the email.

    Returns:
        None: This function does not return any value.
    """
    # Set up your email configuration
    smtp_server = smtp.get("server", None)
    smtp_port = smtp.get("port", 587)
    sender_email = smtp.get("email")
    sender_password = smtp.get("password")
    
    # Create a message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Event Reminder: {event_info['event_name']}"

    # Compose the email body
    body = f"Hello, {recipient_name}!\n\n"
    body += f"This is a reminder for the upcoming event: {event_info['event_name']}.\n"
    body += f"Date: {event_info['event_date']}\n"
    body += f"Location: {event_info['event_location']}\n\n"
    body += "We look forward to seeing you there!\n\n"
    body += "Best regards,\nYour Event Team"

    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        raise Exception("Error sending email:", str(e))

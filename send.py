import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_custom_email(recipient_name, recipient_email, event_info):
    # Set up your email configuration
    smtp_server = "mail.sinimustaahallitustavastaan.org"
    smtp_port = 587  # This may vary depending on your server configuration
    sender_email = "your_email@sinimustaahallitustavastaan.org"
    sender_password = "your_password"

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
        print("Error sending email:", str(e))

# Example usage:
event_details = {
    'event_name': 'Community Gathering',
    'event_date': '2023-09-15',
    'event_location': 'Community Center'
}

recipient_name = 'John Doe'
recipient_email = 'john.doe@example.com'

send_custom_email(recipient_name, recipient_email, event_details)

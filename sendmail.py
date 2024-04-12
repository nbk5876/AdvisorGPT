#------------------------------------------------------------
# sendmail.py
# Purpose: Send an email from gmail
#------------------------------------------------------------
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

gmail_app_password = os.getenv("GMAIL_APP_PASSWORD")
email_from_account = os.getenv("EMAIL_FROM_ACCOUNT")
email_to_account = os.getenv("EMAIL_TO_ACCOUNT")

def send_email(subject, body, to_email):

    print(f"Running send_email with {subject}{body}{to_email}")

    from_email = "tony.byorick@gmail.com"
    from_password = "edtljfdtedukwpcr"  # Use the App Password you generated

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    body = f"{current_time} \n{body}"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    # Log in to server using secure context and send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, message.as_string())


body_content = "Test Message"

# Usage
send_email(
    subject="Advisor Message",
    #body="The quick brown fox jumped over the moon",
    body=body_content,
    to_email="nbk5876@outlook.com"
)

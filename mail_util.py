# mail_util.py
import smtplib
import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email, from_email, from_password):
    print(f"Sending email with from_email: {from_email}")
    print(f"Sending email with from_password: {from_password}")
    print(f"Sending email with to_email: {to_email}")
    print(f"Sending email with subject: {subject}")
    print(f"Sending email with body: {body}")

    # Construct the email message
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"{current_time} \n\n{body}"

    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send the email via Gmail's SMTP server
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, message.as_string())

# This section is typically not necessary in a utility module
# body_content = "Test Message"
# send_email(
#     subject="Advisor Message",
#     body=body_content,
#     to_email="recipient@example.com",
#     from_email="your_gmail_account",
#     from_password="your_app_password"
# )

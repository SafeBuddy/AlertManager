
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SYSTEM_EMAIL = "noa.yaakov@gmail.com"
SYSTEM_EMAIL_PASSWORD = "mrla afql qctg bmme" 

def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SYSTEM_EMAIL
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(SYSTEM_EMAIL, SYSTEM_EMAIL_PASSWORD)
            server.sendmail(SYSTEM_EMAIL, recipient_email, msg.as_string())

        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

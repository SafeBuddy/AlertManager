from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)


SYSTEM_EMAIL = "noa.yaakov@gmail.com"
SYSTEM_EMAIL_PASSWORD = "mrla afql qctg bmme" 


def create_response(success, message, status_code, data=None):
    response = {"success": success, "message": message}
    if data:
        response["data"] = data
    return jsonify(response), status_code



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



@app.route('/alert-parent', methods=['POST'])
def send_alert():
    data = request.json

    if not data or 'user_name' not in data or 'parent_email' not in data:
        return create_response(False, "Invalid request. 'user_name' and 'parent_email' are required.", 400)

    user_name = data['user_name']
    parent_email = data['parent_email']

  
    subject = "Important: Suspicious Activity Detected"
    body = f"""
    Dear Parent,

    We have identified that {user_name} has been communicating with your child and displayed aggressive behavior.
    Please review their messages to ensure your child's safety.

    Best regards,
    SafeBody Team
    """

   
    email_sent = send_email(parent_email, subject, body)

    if email_sent:
        return create_response(True, f"Alert email sent to {parent_email}.", 200)
    else:
        return create_response(False, "Failed to send alert email.", 500)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)

from flask import Flask, request
from email_service import send_email
from utils import create_response



app = Flask(__name__)

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
    app.run(host='127.0.0.1', port=5001)

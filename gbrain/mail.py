import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from dotenv import load_dotenv

load_dotenv()

FROM_EMAIL = "news@xyb.se"
TO_EMAIL = "jeremy.geo@gmail.com"
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")


def send_email(
    subject,
    content,
    to_email=TO_EMAIL,
    from_email=FROM_EMAIL,
):
    message = Mail(from_email, to_email, subject, plain_text_content=content)
    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)

        print(f"Email sent with status code {response.status_code}")
    except Exception as e:
        print(f"Error sending email: {e}")


if __name__ == "__main__":
    send_email(
        subject="Test Email", content="This is a test email sent using SendGrid."
    )

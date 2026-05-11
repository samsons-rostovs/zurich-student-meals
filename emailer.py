import os
import smtplib

from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAILS = [
    email.strip()
    for email in os.getenv("RECEIVER_EMAIL", "").split(",")
    if email.strip()
]


def send_email(meals):

    body = "CHEAPEST MEALS IN ZURICH\n\n"

    for meal in meals:

        body += (
            f"{meal['price']} CHF | "
            f"{meal['mensa']} | "
            f"{meal['category']} | "
            f"{meal['name']}\n"
        )

    msg = MIMEText(body)

    msg["Subject"] = "Cheapest Meals in Zurich"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(RECEIVER_EMAILS)

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(
        EMAIL_ADDRESS,
        EMAIL_PASSWORD
    )

    server.sendmail(
        EMAIL_ADDRESS,
        RECEIVER_EMAILS,
        msg.as_string()
    )

    server.quit()

    print("EMAIL SENT!")
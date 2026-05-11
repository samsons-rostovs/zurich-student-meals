import os
import smtplib

from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")


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
    msg["To"] = RECEIVER_EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.starttls()

    server.login(
        EMAIL_ADDRESS,
        EMAIL_PASSWORD
    )

    server.send_message(msg)

    server.quit()

    print("EMAIL SENT!")
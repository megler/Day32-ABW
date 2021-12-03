# automatedBirthdayWisher.py
#
# Python Bootcamp Day 32 - ABW
# Usage:
#   Sends automated email birthday wishes when today = birthday in csv.
# Day 32 Python Bootcamp
#
# Marceia Egler December 3, 2021

import os, sys, smtplib
from dotenv import load_dotenv
from letter import Letter


letter = Letter()


def send_mail():
    MY_EMAIL = os.getenv("MY_EMAIL")
    MY_PASSWORD = os.getenv("MY_PASSWORD")
    SMTP = os.getenv("SMTP")
    birthday_emails = letter.pick_letter()

    for message in birthday_emails.items():
        msg = "".join(message[1][1])
        with smtplib.SMTP(SMTP, 587) as connection:
            connection.set_debuglevel(1)
            connection.ehlo()
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=message[1][0],
                msg=f"From: {MY_EMAIL}\nSubject: Happy Birthday\n\n{msg}",
            )


def main():
    load_dotenv()
    send_mail()


if __name__ == "__main__":
    sys.exit(main())

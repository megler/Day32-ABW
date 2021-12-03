import datetime as dt
import pandas as pd


class Birthday(object):
    def __init__(self) -> None:
        self.now = dt.datetime.now()
        self.month = self.now.month
        self.day = self.now.day
        self.check_bday = pd.read_csv("birthdays.csv")
        self.bday_month = self.check_bday["month"].astype(int)
        self.bday_day = self.check_bday["day"]
        self.bday_name = self.check_bday["name"]
        self.bday_email = self.check_bday["email"]

    def check_for_birthday(self):
        birthdays = {}
        for i in range(len(self.check_bday)):

            if (
                self.month == self.bday_month[i]
                and self.day == self.bday_day[i]
            ):
                birthdays[self.bday_name[i]] = self.bday_email[i]
        return birthdays

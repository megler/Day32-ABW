from numpy import pi
import pandas as pd
import random
import birthday as birth


class Letter(object):
    def __init__(self) -> None:
        self.birthday = birth.Birthday()
        self.birthday_file = self.birthday.check_bday

    def pick_letter(self) -> None:
        birthdays = self.birthday.check_for_birthday()

        picked_letters = {}
        for name in birthdays:
            rand_letter = random.randint(1, 3)
            with open(
                (f"./letter_templates/letter_{rand_letter}.txt")
            ) as letter:
                lines = letter.readlines()

            new_letter = [item.replace("[NAME]", name) for item in lines]
            picked_letters[name] = birthdays.get(name), new_letter

        return picked_letters

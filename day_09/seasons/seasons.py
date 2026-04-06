from datetime import date

import inflect
import sys


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
        age_in_minutes = get_minutes(birth_date, date.today())
        print(minutes_to_words(age_in_minutes))
    except ValueError:
        sys.exit("Invalid date")


def get_minutes(birth_date, today):
    days = (today - birth_date).days
    if days < 0:
        raise ValueError("Date is in future")
    return days * 24 * 60


def minutes_to_words(minutes):
    p = inflect.engine()
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"


if __name__ == "__main__":
    main()

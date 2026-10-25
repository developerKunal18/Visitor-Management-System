from datetime import datetime
from config import DATETIME_FORMAT


def get_text(prompt):
    """Read non-empty text from the user."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def get_phone():
    """Read and validate a phone number."""
    while True:
        phone = input("Enter phone number: ").strip()
        digits = "".join(character for character in phone if character.isdigit())

        if len(digits) == 10:
            return phone

        print("Please enter a valid 10-digit phone number.")


def current_datetime():
    return datetime.now().strftime(DATETIME_FORMAT)


def pause():
    input("\nPress Enter to continue...")

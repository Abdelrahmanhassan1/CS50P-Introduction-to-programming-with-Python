from validator_collection import validators, checkers, errors


def main():
    try:
        email_address = input("What's your email address? ")
        is_email_address = checkers.is_email(email_address)
        if is_email_address:
            return "Valid"
        return "Invalid"
    except ValueError:
        return "Invalid"


print(main())

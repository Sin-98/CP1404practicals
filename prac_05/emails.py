"""
Emails
Estimate: 25 minutes
Actual:    minutes
"""

def main():
    email_to_name = {}
    email = input("Enter email: ")
    name = get_name_from_email(email)
    checking = input(f"Is your name {name}? (Y/n) ")
    if checking.upper() != "Y" and checking != "":
        name = input("Name: ")
    email_to_name[email] = name


def get_name_from_email(email):
    """Get name from email."""
    possible_name = email.split("@")[0]
    parts = possible_name.split(".")
    name = "".join(parts).title()
    return name

main()
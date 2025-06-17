"""
Emails
Estimate: 25 minutes
Actual:    minutes
"""

def main():
    email_to_name = {}
    email = input("Enter email: ")

def get_name_from_email(email):
    """Get name from email."""
    possible_name = email.split("@")[0]
    parts = possible_name.split(".")
    name = "".join(parts).title()
    return name


MINIMUM_LENGTH = 6
def main():
    """Get password and print asterisks using functions."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks as long as the password."""
    print("*" * len(password))


def get_password():
    """Get valid password according to minimum length."""
    password = input(f"Enter password of minimum length {MINIMUM_LENGTH}: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of minimum length {MINIMUM_LENGTH}: ")
    return password

main()
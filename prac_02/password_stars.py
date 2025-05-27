MINIMUM_LENGTH = 6
def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input(f"Enter password of minimum length {MINIMUM_LENGTH}: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of minimum length {MINIMUM_LENGTH}: ")
    return password

main()
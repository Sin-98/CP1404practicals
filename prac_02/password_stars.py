MINIMUM_LENGTH = 6
password = input(f"Enter password of minimum length {MINIMUM_LENGTH}: ")
while len(password) < MINIMUM_LENGTH:
    password = input(f"Enter password of minimum length {MINIMUM_LENGTH}: ")
print("*" * len(password))
MENU = ("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")

def main():
    """Get score, print result and show stars program."""
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Enter your choice: ").upper()
    print("Farewell")

def get_valid_score():
    """Get a valid score ensuring it meets the requirements."""
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def print_result(score):
    """Display result based on score."""
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

def show_stars(score):
    """Display as many stars as score."""
    print("*" * score)

main()
MENU = ("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")

def main():
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)

def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")

main()
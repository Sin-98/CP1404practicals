"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    """Get score and display its grade."""
    score = float(input("Enter score: "))
    print(determine_grade(score))
    random_score = random.randint(1, 100)
    print(determine_grade(random_score))

def determine_grade(score):
    """Determine the grade of a score."""
    if score < 0 or score > 100:
        return"Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

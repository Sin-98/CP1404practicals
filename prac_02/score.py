"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

def main():
    """Get score and display its grade."""
    score = float(input("Enter score: "))
    print(determine_grade(score))

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

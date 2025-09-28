"""
Menu-driven score program
"""

def main():
    score = get_valid_score()

    choice = ""
    while choice.upper() != "Q":
        print_menu()
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = categorise_scores(score)
            print(f"Result: {result}")
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell! Thanks for using the program.")
        else:
            print("Invalid choice, please try again.")


def print_menu():
    """Display the menu options."""
    print("Menu:\n (G)et a valid score\n (P)rint result\n (S)how stars\n (Q)uit")


def get_valid_score():
    """Prompt user until a valid score (0–100 inclusive) is entered."""
    score = int(input("Enter a valid score (0-100): "))
    if score < 0 or score > 100:
        print("Invalid score, must be between 0 and 100.")
    else :
        print("Please enter a valid number.")
    return score

def categorise_scores(score: float) -> str:
    """categorises users score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print as many stars as the score."""
    print("*" * score)

main()
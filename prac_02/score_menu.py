"""
Menu-driven score program
"""

def main():
    print("Welcome to the Score Program!")
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
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    """Prompt user until a valid score (0–100 inclusive) is entered."""
    score = -1
    while score < 0 or score > 100:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score, must be between 0 and 100.")
        except ValueError:
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
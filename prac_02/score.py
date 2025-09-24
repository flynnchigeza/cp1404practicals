"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = random.randint(0, 100)
    print(f"your score is {score} and it is  {categorise_scores(score)}")


def categorise_scores(score: float) -> str:
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()
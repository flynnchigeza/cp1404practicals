"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Value error will occur when any input string is entered rather than an integer
2. When will a ZeroDivisionError occur?
Zero Division  Error will occur when the denominator is equal to zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
make sure change the denominator input to be greater than zero and if it is less than zero ask them to enter a valid input
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0 :
        denominator = int(input("Enter the denominator"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
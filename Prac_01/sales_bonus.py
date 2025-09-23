"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales"))
bonus = 0
while sales >= 0:
    if sales > 1000:
        bonus_rate= 0.10
    elif sales <= 1000:
        bonus_rate = 0.15
    else:
        print("invalid input")
        break
    bonus = sales * bonus_rate
    print(f"Bonus is ${bonus}")
    sales = float(input("Enter sales"))

number_of_items = int(input("Enter number of items "))
total_price = 0
item_price = 0
while number_of_items < 0:
    print("Invalid number of item")
    number_of_items = int(input("Enter number of items "))
for i in range(number_of_items):
    item_price = float(input("Price of item $"))
    total_price = item_price + total_price
    if total_price > 100:
        total_price = total_price - (total_price * 0.10)
print(f"total price for {number_of_items} items is {total_price:.2f}")

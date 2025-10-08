"""
CP1404 prac 4
list exercises
"""
# basic list operations
numbers = []
for i in range(5):
    number = int(input("number"))
    numbers.append(number)

print("The first number is", numbers[0])
print("The second number is", numbers[1])
print("The smallest number is", min(numbers))
print("The largest number is",max(numbers))
print("The average number is", sum(numbers)/ len(numbers))

# Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
# check if username is valid
username = input("Enter Username")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
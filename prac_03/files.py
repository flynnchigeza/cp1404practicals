#1 Write code that asks the user for their name, then opens a file called name.txt and writes that name to it. Use open and close for this question.
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

#2 In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as above) then prints (note the exact output),
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")

#3 Write code that opens numbers.txt, reads only the first two numbers, adds them together then prints the result, which should be... 59. Use with instead of open and close for this question.
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
print(number1 + number2)

# 4 Now write a fourth block of code that prints the total for all lines in numbers.txt. This should work for a file with any number of numbers. Use with instead of open and close for this question.
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)
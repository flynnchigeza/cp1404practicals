name = str(input("Please enter your name"))
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

choice = str(input(">>>"))
while choice != 'Q':
    if choice == 'H':
        print(f"hello {name}")
    elif choice =='G':
        print(f"Goodbye{name}")
    else:
        print(f"Sorry {name} invalid input,try again")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = str(input(">>>"))
print("finished")



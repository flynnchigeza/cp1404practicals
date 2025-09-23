for i in range(1, 21, 2):
    print(i, end=' ')
print()
#a
for i in range(0,110,10):
     print(i, end=' ')
print()
#b
for i in range(20,0,-1):
    print(i, end=' ')
print()
#c
number_of_stars = int(input("Enter number of Stars"))
for i in range(number_of_stars):
    print('*', end=' ')
#d
number_of_rows = int(input("Enter number of rows"))
for i in range(1,number_of_rows + 1,1):
    print('*' * i)

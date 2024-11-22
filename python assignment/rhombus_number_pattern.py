number = int(input("enter a number for the pattern: "))


space = number



for i in range(1,number+1):

    print(" "*space, end='')
    for j in range(i):
        print(i, end="")
    
    for j in range(i-1, -1, 1):
        print(j, end="")
    
    space -= 1

    print()


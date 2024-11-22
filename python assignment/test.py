n = int(input("enter the number of alphabet for the rhombus pattern?: "))

space = n
# Upper half of rhombus
for i in range(n):
    # Print spaces
    print(" " * space, end="")
    
    # Print first half of letters
    for j in range(i + 1):
        print(chr(65 + (j % 26)), end="")
    
    # Print second half of letters (reverse)
    for j in range(i-1, -1, -1):
        print(chr(65 + (j % 26)), end="")
        
    print()  # New line
    space -= 1

# Lower half of rhombus
space = 2
for i in range(n-2, -1, -1):
    # Print spaces
    print(" " * space, end="")
    
    # Print first half of letters
    for j in range(i + 1):
        print(chr(65 + (j % 26)), end="")
    
    # Print second half of letters (reverse)
    for j in range(i-1, -1, -1):
        print(chr(65 + (j % 26)), end="")
        
    print()  # New line
    space += 1
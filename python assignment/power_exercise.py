# a is index and b is power
n = int(input("enter a number: "))
output = 1
for i in range(1, n+1):
    b = i + 1 #power
    output = i
    if i == 1:
        output = 1
    else:
        for j in range(1, i+1):
            output *= i  #pow(a, b)
    print(f"{i}\t{b}\t{output}")
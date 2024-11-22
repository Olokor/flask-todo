n = int(input("enter the number of alphabet for the rhombus pattern?: "))

alphabet = ""
letter_id = 0
for i in range(n):
    alphabet += chr(65+letter_id)
    letter_id += 1
    if letter_id > 25:
        letter_id = 0

space = n
j = n-2
for i in range((n + (n-1))):
    if i < n:
        print(" "*space+alphabet[:i]+alphabet[i::-1])
        space -=1
    if i >= n:
        print(" "*(space+2)+alphabet[:j] + alphabet[j::-1] )
        # print("yes")
        j-=1
        space += 1
        
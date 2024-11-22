n = int(input("enter the number of alphabet for the rhombus pattern?: "))

alphabet = ""
letter_id = 0
for i in range(n):
    alphabet += chr(65+letter_id)
    letter_id += 1
    if letter_id > 25:
        letter_id = 0
        
    

space1 = n
space2 = 0
for i in range(n+2):
    if i < n:
        if i == 0:
            result = alphabet[i]
            print(" "*(space1-1)+result)
        for j in range(i):
            result = alphabet[:i] + alphabet[i-j-1::-1]
            if len(result) %2 != 0:
                print(" "*space1+result)
                break
    elif i > n:
        # print("it's happening")
        for j in range(i+1):
            # print(alphabet[:i-j])
            result = alphabet[:i-j] + alphabet[i-j::-1]
            if len(result) % 2 != 0:
                print(" "*(space2-2)+result)
            space2 +=1

    
                

    
    space1 -= 1
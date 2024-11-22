
for i in range(number*2):
    if i <= number-1:
        print( " "*space+number_array[i::-1] + number_array[1:i+1])
        space -= 1
    if i > number:
        print(" "*(space +2)+number_array[j::-1] + number_array[1:j+1])
        j -= 1
        space += 1
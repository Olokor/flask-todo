def get_max(array:list):
	max_number = array[0]
	for i in array:
		if i > maxNumber:
			maxNumber = i
	return maxNumber

print(get_max(7))
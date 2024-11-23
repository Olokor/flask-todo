def get_max(array:list):
	if type(array) is list:
		max_number = array[0]
		for i in array:
			if i > max_number:
				max_number = i
		return max_number
	raise TypeError

def reverse_list(array:list):
	if type(array) is list:
		reversed_array = []
		for i in range((len(array)-1), -1, -1):
			reversed_array.append(array[i])
		return reversed_array
	raise TypeError
def elementExist(element, array:list):
	if type(array) is list:
		if element in array:
			return True
		return False
	raise TypeError

def print_odd_index_values(array:list):
	if type(array) is list:
		odd_array = []
		for i in range(1, len(array), 2):
			print(array[i], end=",")
			odd_array.append(array[i])
		return odd_array
	raise TypeError



print(print_odd_index_values([1,2,3,4,5,6,7,8,9]))
		





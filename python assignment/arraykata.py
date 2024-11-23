def get_max(array:list):
	if type(array) is list and array_contain_only_numbers(array):
		max_number = array[0]
		for i in array:
			if i > max_number:
				max_number = i
		return max_number
	raise TypeError

def reverse_list(array:list):
	if type(array) is list and array_contain_only_numbers(array): return array[::-1]
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



def print_even_index_values(array:list):
	if type(array) is list:
		even_array = []
		for i in range(0, len(array), 2):
			print(array[i], end=",")
			even_array.append(array[i])
		return even_array
	raise TypeError

def array_contain_only_numbers(array):
	for i in array:
		if type(i) not in [int, float]:
			return False
	return True
def sum_array_element(array:list):
	if type(array) is list:
		if array_contain_only_numbers:
			sum = 0
			for i in array:
				sum += i
		return sum
	raise TypeError

def check_palindrome(text:str):
	if type(text) is str:
		palindrome = text[::-1]
		if text == palindrome:
			return palindrome
		return "does not have a possible palindrome"
	raise TypeError





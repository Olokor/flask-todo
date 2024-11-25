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

# use this function where necessary!
def array_contain_only_numbers(array):
	for i in array:
		if type(i) not in [int, float]:
			return False
	return True
def sum_array_element(array:list): #implemented with for loop
	if type(array) is list and array_contain_only_numbers(array):
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
def sum_of_array_element(array:list): #implemented with while loop
	if type(array) is list and array_contain_only_numbers(array):
		sum = 0
		array_index = 0
		iter = len(array)
		while iter !=0:
			sum += array[array_index]
			array_index += 1
			iter -= 1
		return sum
	raise TypeError

def concatenate_arrays(array1:list, array2:list):
	if type(array1) is list and type(array2) is list:

		return array1 + array2
	raise TypeError

def return_short_array_length(array1:list, array2:list):
	if len(array1) == len(array2) or len(array1) < len(array2):
		return len(array1), array1
	return len(array2), array2

def concatenate_arrays_by_alternating_elements(array1:list, array2:list):
	if type(array1) is list and type(array2) is list:
		final_array = []
		if len(array1) == len(array2):
			for i in range(len(array1)):
				final_array.append(array1[i])
				final_array.append(array2[i])
			return final_array
		for i in range(return_short_array_length(array1,array2)[0]):
			final_array.append(array1[i])
			final_array.append(array2[i])
		if return_short_array_length(array1, array2)[1] == array1:
			final_array += array2[len(array1):]
			return final_array
		final_array += array1[len(array2):]

		return final_array
	
	raise TypeError


def number_to_array(number:int):
	if type(number) is int:
		array = []
		for i in str(number):
			array.append(int(i))
		return array
	raise TypeError



		
				
			
		




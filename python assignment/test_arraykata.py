from unittest import TestCase
from arraykata import *

class TestArrayKata(TestCase):
	def test_that_get_max_function_exists(self):
		get_max([0])

	def test_that_function_returns_correct_result(self):
		actual = get_max([1,2,3,5,4])
		expected = 5
		self.assertEqual(actual, expected)

	def test_that_error_raised_if_list_not_passed(self):
		self.assertRaises(TypeError, get_max, "45", 777)
	
	def test_that_reverse_list_exists(self):
		reverse_list([0])
	
	def test_that_reverse_list_returns_correct_result(self):
		actual_result = reverse_list([1,3,6,7,9])
		expected_result = [9,7,6,3,1]
		self.assertEqual(actual_result, expected_result)
	


	def test_that_reverse_list_raised_error_if_list_not_passed(self):
		self.assertRaises(TypeError, reverse_list, [1,2,3,5,"5"])

	def test_that_elementExist_exist(self):
		elementExist(5, [1,2,3,4,5])

	def test_that_elementExist_returns_correct_result(self):
		actual_result = elementExist(5, [1,2,3,4,5])
		expected_result = True
		self.assertEqual(actual_result, expected_result)


	def test_that_elementExist_raised_error_if_list_not_passed(self):
		self.assertRaises(TypeError, elementExist, "5", "yer")

	
	def test_that_print_odd_index_values_exist(self):
		print_odd_index_values([1,2,3,4])
	
	def test_that_print_odd_index_values_returns_correct_result(self):
		actual_result = print_odd_index_values([1,2,3,4,5,6,7,8,9])
		expected_result = [2,4,6,8]
		self.assertEqual(actual_result, expected_result)

	def test_that_print_odd_index_values_raise_error_if_list_not_passed(self):
		self.assertRaises(TypeError, print_odd_index_values, "33")


	def test_that_print_even_index_values_exists(self):
		print_even_index_values([])


	def test_that_print_even_index_values_return_correct_result(self):
		actual_result = print_even_index_values([1,2,3,4,5,6,7,8,9])
		expected_result = [1,3,5,7,9]
		self.assertEqual(actual_result, expected_result)

	def test_that_print_even_index_values_raise_error_if_list_not_passed(self):
		self.assertRaises(TypeError, print_even_index_values, "677")

	def test_that_sum_array_element_exist(self):
		sum_array_element([1,2,3])

	def test_that_sum_array_element_return_correct_result(self):
		actual_result = sum_array_element([1,3,5])
		expected_result = 9
		self.assertEqual(actual_result, expected_result)

	def test_that_sum_array_element_raise_error_if_list_not_passed(self):
		self.assertRaises(TypeError, sum_array_element, "567")

	def test_that_check_palindrome_exists(self):
		check_palindrome("aba")
	
	def test_that_check_palindrome_return_correct_result(self):
		actual_result = check_palindrome("aba")
		expected_result = "aba"
		self.assertEqual(actual_result, expected_result)



		

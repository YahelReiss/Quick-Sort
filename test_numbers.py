import unittest
from quickSort import quick_sort
import time


class MyTestCase(unittest.TestCase):
    def test_simple_case(self):
        arr = [3, 1, 4, 11, 5, 9, 2, 6, 7, 8, 10]
        arr2 = [3, 1, 4, 11, 5, 9, 2, 6, 7, 8, 10]
        quick_sort(0, len(arr), sorted(arr2))
        self.assertEqual(arr, arr2)

    def test_equal_elements(self):
        arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        arr2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        quick_sort(0, len(arr), sorted(arr2))
        self.assertEqual(arr, arr2)

    def test_negative(self):
        arr = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        arr2 = [-3, -1, -4, -1, -5, -9, -2, -6, -5, -3, -5]
        quick_sort(0, len(arr), sorted(arr2))
        self.assertEqual(arr, arr2)

    def test_all_equal(self):
        arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        arr2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        quick_sort(0, len(arr), sorted(arr2))
        self.assertEqual(arr, arr2)

    def test_sorted_arr(self):
        arr = [1, 2, 3, 4, 5, 6, 7]
        arr2 = [1, 2, 3, 4, 5, 6, 7]
        quick_sort(0, len(arr), sorted(arr2))
        self.assertEqual(arr, arr2)

    def test_reversed_sorted_arr(self):
        arr = [7, 6, 5, 4, 3, 2, 1]
        arr2 = [7, 6, 5, 4, 3, 2, 1]
        quick_sort(0, len(arr), sorted(arr2))
        self.assertEqual(arr, arr2)

    def test_empty_array(self):
        arr = []
        arr2 = []
        quick_sort(0, len(arr), arr)
        self.assertEqual(arr, arr2)

    def test_single_element_array(self):
        arr = [42]
        arr2 = [42]
        quick_sort(0, len(arr), arr)
        self.assertEqual(arr, sorted(arr2))

    def test_large_array(self):
        arr = list(range(10000, 0, -1))
        arr2 = list(range(1, 10001))
        quick_sort(0, len(arr), arr)
        self.assertEqual(arr, arr2)

    def test_array_with_strings(self):
        arr = ['banana', 'apple', 'orange', 'grape', 'pineapple']
        arr2 = ['banana', 'apple', 'orange', 'grape', 'pineapple']
        quick_sort(0, len(arr), arr)
        self.assertEqual(arr, sorted(arr2))

    def test_array_with_floating_point_numbers(self):
        arr = [3.5, 1.2, 4.8, 2.3, 5.7, 9.1, 6.4]
        arr2 = [3.5, 1.2, 4.8, 2.3, 5.7, 9.1, 6.4]
        quick_sort(0, len(arr), arr)
        self.assertEqual(arr, sorted(arr2))

    def test_performance(self):
        # Test case for performance testing
        sizes = [10000, 100000, 1000000]  # Array sizes to test
        for size in sizes:
            arr = list(range(size, 0, -1))  # Array of integers from size to 1 in descending order
            start_time = time.time()
            quick_sort(0, len(arr), arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Sorting an array of size {size} took {execution_time:.6f} seconds.")

        for size in sizes:
            arr = list(range(size, 0, -1))  # Array of integers from size to 1 in descending order
            start_time = time.time()
            sorted(arr)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Sorting an array of size {size} took {execution_time:.6f} seconds.")


if __name__ == '__main__':
    unittest.main()

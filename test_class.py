import unittest
from Person import Person
from quickSort import quick_sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p1, p2, p3, p4, p5]
        quick_sort(0, len(arr), arr)
        res = []
        self.assertEqual(res, sorted(res))

    def test_reversed_sorted(self):
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p5, p4, p3, p2, p1]
        quick_sort(0, len(arr), arr)
        res = []
        self.assertEqual(res, sorted(res))

    def test_sort_by_name(self):
        # Test case sorting Persons by name
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p1, p2, p3, p4, p5]
        for p in arr:
            p.id = p.name

        quick_sort(0, len(arr), arr)
        res = []
        self.assertEqual(res, sorted(res))

    def test_negative(self):
        # Test case sorting Persons by name
        p1 = Person("Yahel")
        p2 = Person("Yoav")
        p3 = Person("Tal")
        p4 = Person("Amit")
        p5 = Person("Gal")
        arr = [p1, p2, p3, p4, p5]
        p1.id = -7
        p2.id = -14.5
        p3.id = 0
        p4.id = 24

        quick_sort(0, len(arr), arr)
        res = []
        self.assertEqual(res, sorted(res))


if __name__ == '__main__':
    unittest.main()

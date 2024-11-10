import unittest
from app import add, subtract, multiply, divide

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 3), 1)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(1000, 2000), 3000)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
        self.assertEqual(subtract(2000, 1000), 1000)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-2, 3), -6)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1000, 2000), 2000000)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-6, 3), -2)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(1000, 2), 500)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_large_numbers(self):
        self.assertEqual(add(10**6, 10**6), 2 * 10**6)
        self.assertEqual(subtract(10**6, 10**5), 900000)
        self.assertEqual(multiply(10**4, 10**4), 10**8)
        self.assertEqual(divide(10**6, 10**3), 1000)

    def test_small_numbers(self):
        self.assertEqual(subtract(0.0002, 0.0001), 0.0001)
        self.assertEqual(multiply(0.0001, 0.0002), 0.00000002)
        self.assertEqual(divide(0.0002, 0.0001), 2)

    def test_negative_large_numbers(self):
        self.assertEqual(add(-10**6, -10**6), -2 * 10**6)
        self.assertEqual(subtract(-10**6, -10**5), -900000)
        self.assertEqual(multiply(-10**4, -10**4), 10**8)
        self.assertEqual(divide(-10**6, -10**3), 1000)

    def test_edge_cases(self):
        self.assertEqual(add(0, -1), -1)
        self.assertEqual(subtract(0, 1), -1)
        self.assertEqual(multiply(0, 1), 0)
        self.assertEqual(divide(0, 1), 0)
        self.assertEqual(divide(1, 1), 1)
        self.assertEqual(add(1.5, 2.5), 4)

    def test_multiply_by_1_and_0(self):
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide_by_float(self):
        self.assertEqual(divide(7, 2.5), 2.8)
        self.assertEqual(divide(9, 3.0), 3.0)

if __name__ == '__main__':
    unittest.main()

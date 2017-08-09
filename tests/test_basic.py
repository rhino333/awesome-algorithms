import unittest
from algorithms.basic import Basic


class TestBasic(unittest.TestCase):

    def test_factorial(self):
        self.assertEquals(Basic.factorial(5), 120)

    def test_fibonacci(self):
        self.assertEquals(Basic.fibonacci(0), 0)
        self.assertEquals(Basic.fibonacci(1), 1)
        self.assertEquals(Basic.fibonacci(2), 1)
        self.assertEquals(Basic.fibonacci(3), 2)
        self.assertEquals(Basic.fibonacci(4), 3)
        self.assertEquals(Basic.fibonacci(5), 5)
        self.assertEquals(Basic.fibonacci(6), 8)
        self.assertEquals(Basic.fibonacci(7), 13)
        self.assertEquals(Basic.fibonacci(8), 21)
        self.assertEquals(Basic.fibonacci(9), 34)
        self.assertEquals(Basic.fibonacci(31), 1346269)

    def test_time_conversion(self):
        self.assertEquals(Basic.time_conversion('07:05:45PM'), '19:05:45')
        self.assertEquals(Basic.time_conversion('12:40:22AM'), '00:40:22')
        self.assertEquals(Basic.time_conversion('12:45:54PM'), '12:45:54')




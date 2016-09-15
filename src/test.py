import unittest
from lib import math_cal


class MyTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_calculator(self):
        calculator = math_cal.MathExpressionsCal()
        self.assertEqual(first=calculator.execute_it("(1+1)*2"), second=4.0)
        self.assertEqual(first=calculator.execute_it("1+1"), second=2.0)
        self.assertEqual(first=calculator.execute_it("((1+1))"), second=2.0)
        self.assertEqual(first=calculator.execute_it("2+(1-1)*5"), second=2.0)
        self.assertEqual(first=calculator.execute_it("1+(1*1)"), second=2.0)
        self.assertEqual(first=calculator.execute_it("sin(90)"), second=1.0)
        self.assertEqual(first=calculator.execute_it("cos(60)"), second=0.5000000000000001)
        self.assertEqual(first=calculator.execute_it("log(10,100)"), second=2.0)


if __name__ == "__main__":
    my_test = MyTest()
    my_test.test_calculator()

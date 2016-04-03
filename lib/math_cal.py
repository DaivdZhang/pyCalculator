"""this extension try to enhance the function of the calculator"""

from lib import basic_cal
import math


class MathExpressionsCal(basic_cal.Calculator):
    def __init__(self):
        super().__init__()
        self.math_operator_list = {"sin": -1, "cos": -1, "tan": -1, "log": -1, ',': -1, "ln": -1}
        self.math_operate = {"sin": "_sin_it", "cos": "_cos_it", "tan": "_tan_it", ",": "_pass_it",
                             "ln": "_log_it"}
        self.binary_math_operate = {"log": "_log_it"}
        self.operator_list.update(self.math_operator_list)
        self.operate.update(self.binary_math_operate)
        self.PI = math.pi

    def _sin_it(self, x):
        return math.sin(x*self.PI/180)

    def _cos_it(self, x):
        return math.cos(x*self.PI/180)

    def _tan_it(self, x):
        return math.tan(x*self.PI/180)

    @staticmethod
    def _log_it(a=math.e, b=math.e):
        try:
            return math.log(b, a)
        except ZeroDivisionError as error:
            print(error)

    @staticmethod
    def _pass_it(x):
        return x

    def load_expressions(self, expressions):
        super().load_expressions(expressions)

    def parse_expressions(self):
        super().parse_expressions()

    def calculate_expressions(self):
        for element in self.expressions:
            if element not in self.operator_list:
                self.stack.append(element)
            elif element in self.math_operate:
                x = float(self.stack.pop())
                calculate = getattr(self, self.math_operate[element])
                self.stack.append(calculate(x))
            else:
                a = float(self.stack.pop())
                b = float(self.stack.pop())
                calculate = getattr(self, self.operate[element])
                self.stack.append(calculate(b, a))
        return self.stack.pop()

    def clear_stack(self):
        super().clear_stack()

    def execute_it(self, expressions):
        self.load_expressions(expressions)
        self.check_invalid_expressions()
        self.parse_expressions()
        answer = self.calculate_expressions()
        self.previous_answer = answer
        print("answer = %s" % answer)
        self.clear_stack()
        return answer


if __name__ == "__main__":
    math_cal = MathExpressionsCal()
    math_cal.execute_it("log(10,100)")

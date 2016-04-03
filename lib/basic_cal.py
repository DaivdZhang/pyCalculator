"""try making a calculator"""


class Calculator(object):
    def __init__(self):
        self.stack = []
        self.expressions = []
        self.operator_list = {'+': 2, '-': 2, '*': 1, '/': 1, '(': -1, ')': -1, '^': 0, ',': -1}
        self.operate = {'+': "_add_it", '-': "_minus_it", '*': "_multiply_it", '/': "_divide_it",
                        '^': "_pow_it"}
        self.previous_answer = 0

    @staticmethod
    def _add_it(x, y):
        return x + y

    @staticmethod
    def _minus_it(x, y):
        return x - y

    @staticmethod
    def _multiply_it(x, y):
        return x * y

    @staticmethod
    def _divide_it(x, y):
        try:
            return x / y
        except ZeroDivisionError as error:
            print(error)

    @staticmethod
    def _pow_it(x, y):
        return x ** y

    def load_expressions(self, expressions):
        temp = ""
        i = 0
        if expressions[0] in {'-', '+'}:
            expressions = '0' + expressions
        for character in expressions:
            if character not in self.operator_list:
                temp += character
                continue
            if temp != "":
                self.expressions.append(temp)
            temp = ""
            self.expressions.append(character)
            if character == '(' and expressions[i+1] in {'-', '+'}:
                self.expressions.append('0')
            i += 1
        self.expressions.append(temp)
        self.expressions.reverse()
        if "" in self.expressions:
            while True:
                self.expressions.remove("")
                if "" not in self.expressions:
                    break

    def check_invalid_expressions(self):
        """
        prevent invalid expressions from inputting
        """
        operator_index = []
        operator_set = {'+', '-', '*', '/'}
        i = 0
        for element in self.expressions:
            if element in self.operator_list:
                operator_index.append(i)
            i += 1
        operator_index.reverse()
        while True:
            try:
                i = operator_index.pop()
                if self.expressions[i-1] in operator_set and self.expressions[i+1] in operator_set:
                    print("Syntax Error!")
                    break
            except IndexError:
                break

    def parse_expressions(self):
        """
        turn the expressions into postfix expressions
        """
        temp_stack = []
        output = []
        while True:
            try:
                temp = self.expressions.pop()
                if temp not in self.operator_list:
                    output.append(temp)
                elif temp == '(':
                    temp_stack.append(temp)
                elif temp == ')':
                    while temp_stack[-1] != '(':
                        output.append(temp_stack.pop())
                    temp_stack.pop()
                else:
                    if temp_stack:
                        if temp_stack[-1] == '(':
                            temp_stack.append(temp)
                        elif self.operator_list[temp] >= self.operator_list[temp_stack[-1]]:
                            output.append(temp_stack.pop())
                            temp_stack.append(temp)
                        else:
                            temp_stack.append(temp)
                    else:
                        temp_stack.append(temp)
            except IndexError:
                break
        temp_stack.reverse()
        self.expressions = output + temp_stack

    def calculate_expressions(self):
        for element in self.expressions:
            if element not in self.operator_list:
                self.stack.append(element)
            else:
                a = float(self.stack.pop())
                b = float(self.stack.pop())
                calculate = getattr(self, self.operate[element])
                self.stack.append(calculate(b, a))
        return self.stack.pop()

    def clear_stack(self):
        self.stack.clear()
        self.expressions.clear()

    def execute_it(self, expressions):
        self.load_expressions(expressions)
        self.check_invalid_expressions()
        self.parse_expressions()
        answer = self.calculate_expressions()
        self.previous_answer = answer
        self.clear_stack()
        print(float(answer))
        return float(answer)


if __name__ == "__main__":
    calculator = Calculator()
    calculator.execute_it("1+1")

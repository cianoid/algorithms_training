class Calculator:
    def __init__(self):
        self.stack_value = []
        self.stack_operator = []

    def add_expressions(self, expressions):
        for expr in expressions:
            try:
                self.add_value(int(expr))
            except ValueError:
                self.add_action(expr)

    def add_value(self, value):
        self.stack_value.append(value)

    def add_action(self, operation):
        self.stack_operator.append(operation)

        self.calculate()

    def get_result(self):
        return self.stack_value.pop()

    def __process_numbers(self, number1, number2, action):
        if action == '+':
            return number2 + number1
        if action == '-':
            return number2 - number1
        if action == '*':
            return number2 * number1
        if action == '/':
            return number2 // number1

    def calculate(self):
        len_stack_operator = len(self.stack_operator)
        len_stack_value = len(self.stack_value)

        # print('values =', self.stack_value, 'operators =', self.stack_operator)

        if len_stack_operator == 0:
            return

        if len_stack_value == 3:
            self.add_value(
                self.__process_numbers(
                    self.stack_value.pop(), self.stack_value.pop(),
                    self.stack_operator.pop()))

            return

        action = self.stack_operator.pop()
        # if len_stack_value == 2:
        number2 = self.stack_value.pop()
        # else:
        #     number2 = self.result
        number1 = self.stack_value.pop()

        self.add_value(self.__process_numbers(number1, number2, action))


if __name__ == '__main__':
    input_expressions = input().split()

    calc = Calculator()
    calc.add_expressions(input_expressions)
    print(calc.get_result())

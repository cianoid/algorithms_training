#ID успешной посылки: 68060204

class Calculator:
    def __init__(self):
        self.values = []

    def add_expressions(self, expressions):
        for expr in expressions:
            try:
                self.add_value(int(expr))
            except ValueError:
                self.calculate(expr)

    def add_value(self, value):
        self.values.append(value)

    def get_result(self):
        return self.values.pop()

    def calculate(self, action):
        number1 = self.values.pop()
        number2 = self.values.pop()

        if action == '+':
            self.add_value(number2 + number1)
        if action == '-':
            self.add_value(number2 - number1)
        if action == '*':
            self.add_value(number2 * number1)
        if action == '/':
            self.add_value(number2 // number1)


if __name__ == '__main__':
    calc = Calculator()
    calc.add_expressions(input().split())
    print(calc.get_result())

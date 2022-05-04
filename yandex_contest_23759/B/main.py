#ID успешной посылки: 68078536

class StackIsEmpty(Exception):
    pass


class Stack:
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
        if len(self.values) == 0:
            raise StackIsEmpty('Стек значений пуст. Выход из программы')

        return self.values.pop()

    def calculate(self, action):
        number1 = self.values.pop()
        number2 = self.values.pop()

        actions = {
            '+': lambda n1, n2: n2 + n1,
            '-': lambda n1, n2: n2 - n1,
            '*': lambda n1, n2: n2 * n1,
            '/': lambda n1, n2: n2 // n1
        }

        self.add_value(actions[action](number1, number2))


if __name__ == '__main__':
    calc = Stack()
    calc.add_expressions(input().split())
    print(calc.get_result())

class StackMax:
    stack = []
    max = 0

    def __init__(self):
        self.stack = []
        self.max = None

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        try:
            self.stack.pop()
        except IndexError:
            print('error')

    def get_max(self):
        try:
            print(max(self.stack))
        except ValueError:
            print('None')


if __name__ == '__main__':
    command_count = int(input())

    stack = StackMax()

    while command_count > 0:
        command = input().split()

        func_name = command[0]

        if len(command) == 2:
            getattr(stack, func_name)(int(command[1]))
        else:
            getattr(stack, func_name)()

        command_count -= 1

class StackMaxEffective:
    stack = []
    maxstack = []
    max = None

    def __init__(self):
        self.maxstack.append(self.max)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, x):
        if self.max is None or self.max <= x:
            self.max = x
            self.maxstack.append(self.max)

        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            self.max = None
            self.maxstack = [self.max]
            print('error')
            return

        popped = self.stack.pop()
        if popped == self.max:
            self.maxstack.pop()
            self.max = self.maxstack[-1]

    def get_max(self):
        print(self.max)


if __name__ == '__main__':
    command_count = int(input())

    stack = StackMaxEffective()

    while command_count > 0:
        command = input().split()

        func_name = command[0]

        if len(command) == 2:
            getattr(stack, func_name)(int(command[1]))
        else:
            getattr(stack, func_name)()

        command_count -= 1

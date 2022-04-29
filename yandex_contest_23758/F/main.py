class StackMax:
    stack = []
    max = 0

    def __init__(self):
        self.stack = []
        self.max = None

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, x):
        if self.max is None or x > self.max:
            self.max = x

        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            print('error')
            return False

        return self.stack.pop()

    def get_max(self):
        if self.is_empty():
            print(None)
            return False

        return self.max


if __name__ == '__main__':
    stack = StackMax()

    print(stack.is_empty())

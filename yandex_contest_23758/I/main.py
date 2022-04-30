class MyQueueSized:
    def push(self, x):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass


if __name__ == '__main__':
    command_count = int(input())

    stack = MyQueueSized()

    while command_count > 0:
        command = input().split()

        func_name = command[0]

        if len(command) == 2:
            getattr(stack, func_name)(int(command[1]))
        else:
            getattr(stack, func_name)()

        command_count -= 1

class Node:
    def __init__(self, x):
        self.value = x
        self.next = None

    def __str__(self):
        return str(self.value)


class ConnectedQueue:
    last = None
    first = None

    def __init__(self):
        self.queue_size = 0

    def get(self):
        if self.queue_size == 0:
            print('error')
            return

        print(self.first)
        self.first = self.first.next
        self.queue_size -= 1

    def put(self, x):
        current = Node(x)

        if self.queue_size > 0:
            self.last.next = current
        else:
            self.first = current

        self.last = current
        self.queue_size += 1

    def size(self):
        print(self.queue_size)


if __name__ == '__main__':
    command_count = int(input())

    queue = ConnectedQueue()

    while command_count > 0:
        command = input().split()

        func_name = command[0]

        if len(command) == 2:
            # print(f'>> {func_name}({command[1]})')
            getattr(queue, func_name)(int(command[1]))
        else:
            # print(f'>> {func_name}()')
            getattr(queue, func_name)()

        command_count -= 1

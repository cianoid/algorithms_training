class MyQueueSized:
    max_size = 0
    queue_size = 0
    head = 0
    tail = 0
    queue: list

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size

    def push(self, x):
        if self.queue_size == self.max_size:
            print('error')
            return

        self.queue[self.tail] = x
        self.queue_size += 1
        self.tail += 1

        if self.tail == -1:
            self.tail = self.max_size - 1
        elif self.tail == self.max_size:
            self.tail = 0

    def pop(self):
        if self.is_empty():
            print(None)
            return

        popped = self.queue[self.head]
        self.head += 1
        self.queue_size -= 1

        if self.head == -1:
            self.head = self.max_size - 1
        elif self.head == self.max_size:
            self.head = 0

        print(popped)

    def peek(self):
        if self.is_empty():
            print(None)
            return

        print(self.queue[self.head])

    def size(self):
        print(self.queue_size)

    def is_empty(self):
        return self.queue_size == 0


if __name__ == '__main__':
    command_count = int(input())
    queue_size = int(input())

    queue = MyQueueSized(queue_size)

    while command_count > 0:
        command = input().split()

        func_name = command[0]

        if len(command) == 2:
            getattr(queue, func_name)(int(command[1]))
        else:
            getattr(queue, func_name)()

        command_count -= 1

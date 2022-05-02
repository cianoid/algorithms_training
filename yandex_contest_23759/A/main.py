# ID посылки: 68004468

class Deque:
    def __init__(self, deque_max_size):
        self.deque_max_size = deque_max_size
        self.deque = [None] * deque_max_size
        self.deque_size = 0
        self.head = 0
        self.tail = 0

    def __is_empty(self):
        return self.deque_size == 0

    def __is_full(self):
        return self.deque_size == self.deque_max_size

    def push_back(self, value):
        if self.__is_full():
            print('error')
            return

        self.deque[self.tail] = value

        self.deque_size += 1
        self.tail += 1

        if self.tail == self.deque_max_size:
            self.tail = 0

    def push_front(self, value):
        if self.__is_full():
            print('error')
            return

        self.head -= 1
        if self.head < 0:
            self.head = self.deque_max_size - 1

        self.deque[self.head] = value
        self.deque_size += 1

    def pop_front(self):
        if self.__is_empty():
            print('error')
            return

        print(self.deque[self.head])

        self.deque[self.head] = None
        self.head += 1
        self.deque_size -= 1

        if self.head == self.deque_max_size:
            self.head = 0

    def pop_back(self):
        if self.__is_empty():
            print('error')
            return

        self.tail -= 1
        if self.tail < 0:
            self.tail = self.deque_max_size - 1

        print(self.deque[self.tail])
        self.deque[self.tail] = None
        self.deque_size -= 1


if __name__ == '__main__':
    command_count = int(input())

    queue = Deque(int(input()))

    while command_count > 0:
        command = input().split()

        func_name = command[0]

        if len(command) == 2:
            getattr(queue, func_name)(int(command[1]))
        else:
            getattr(queue, func_name)()

        command_count -= 1

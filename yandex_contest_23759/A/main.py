# ID посылки: 68004468

class StackOverflow(Exception):
    pass


class Deque:
    def __init__(self, deque_max_size):
        self.deque_max_size = deque_max_size
        self.deque = [None] * deque_max_size
        self.deque_size = 0
        self.head = 0
        self.tail = 0

    def __exception_if_empty(self):
        if self.deque_size == 0:
            raise StackOverflow

    def __exception_if_full(self):
        if self.deque_size == self.deque_max_size:
            raise StackOverflow

    def push_back(self, value):
        self.__exception_if_full()

        self.deque[self.tail] = value

        self.deque_size += 1
        self.tail += 1

        if self.tail == self.deque_max_size:
            self.tail = 0

    def push_front(self, value):
        self.__exception_if_full()

        self.head -= 1
        if self.head < 0:
            self.head = self.deque_max_size - 1

        self.deque[self.head] = value
        self.deque_size += 1

    def pop_front(self):
        self.__exception_if_empty()

        result = self.deque[self.head]

        self.deque[self.head] = None
        self.head += 1
        self.deque_size -= 1

        if self.head == self.deque_max_size:
            self.head = 0

        return result

    def pop_back(self):
        self.__exception_if_empty()

        self.tail -= 1
        if self.tail < 0:
            self.tail = self.deque_max_size - 1

        result = self.deque[self.tail]
        self.deque[self.tail] = None
        self.deque_size -= 1

        return result


if __name__ == '__main__':
    command_count = int(input())

    queue = Deque(int(input()))

    while command_count > 0:
        try:
            command = input().split()
            func_name = command[0]

            if len(command) == 2:
                func_result = getattr(queue, func_name)(int(command[1]))
            else:
                func_result = getattr(queue, func_name)()

            if func_result is not None:
                print(func_result)

        except StackOverflow:
            print('error')

        command_count -= 1

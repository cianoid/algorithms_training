# Comment it before submitting
class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        sl = list()

        if self.prev:
            sl.append(f'{self.value}.prev = {self.prev.value}')
        if self.next:
            sl.append(f'{self.value}.next = {self.next.value}')

        return ', '.join(sl)


def solution(node):
    while node:
        repl = node.prev
        node.prev = node.next
        node.next = repl

        if node.prev is None:
            break

        node = node.prev

    return node


def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)

    print(new_head)


if __name__ == '__main__':
    test()

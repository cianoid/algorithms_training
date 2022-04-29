# Comment it before submitting
class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    xnode = node
    counter = 0

    while node:
        if idx == 0:
            return node.next_item

        if not node.next_item.next_item:
            break

        if idx > 0 and idx == counter + 1:
            node.next_item = node.next_item.next_item

        node = node.next_item
        counter += 1

    return xnode


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 4)

    print(new_head)


if __name__ == '__main__':
    test()

# coding=utf-8
"""
2 класса реализующих циклический буфер FIFO. Плюсы и Минусы каждого
"""


class First:
    def __init__(self):
        self.data = []
        self.index = 0

    def append(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data) > 1:
            self.data = self.data[1:]
        else:
            self.data = []

    def __repr__(self):
        return " ".join(map(str, self.data))

    def __iter__(self):
        while self.index != len(self.data):
            yield self.data[self.index % len(self.data)]
            self.index += 1


class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Second:
    def __init__(self):
        self.current = self.head = self.tail = None

    def append(self, value):
        t = self.head

        if t is None:
            self.current = self.head = self.tail = Node(value, self.head)
            return

        while t != self.tail:
            t = t.next_node

        t.next_node = Node(value, self.head)
        self.tail = t.next_node

        return

    def pop(self):
        t = self.head.next_node
        del self.head
        self.current = self.head = self.tail.next_node = t

    def __iter__(self):
        while True:
            yield self.current.value
            self.current = self.current.next_node

            if self.current == self.head:
                break


if __name__ == '__main__':
    print " == Example 1 =="
    arr1 = First()

    arr1.append(1)
    arr1.append(2)
    arr1.append(3)
    arr1.append(4)
    arr1.append(5)
    arr1.append(6)

    arr1.pop()

    for x in arr1:
        print x

    print "== Example 2 =="

    arr2 = Second()

    arr2.append(1)
    arr2.append(2)
    arr2.append(3)
    arr2.append(4)
    arr2.append(5)
    arr2.append(6)

    arr2.pop()

    for x in arr2:
        print x

class Node:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.length = 0

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        return False

    def append(self, value: int) -> None:
        newNode = Node(value)
        if self.length == 0:
            newNode.prev = self.head
            newNode.next = self.tail
            self.head.next = newNode
            self.tail.prev = newNode
        else:
            prev = self.tail.prev
            newNode.next = prev.next
            newNode.prev = prev
            prev.next = newNode
            self.tail.prev = newNode

        self.length += 1

    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        if self.length == 0:
            newNode.prev = self.head
            newNode.next = self.tail
            self.head.next = newNode
            self.tail.prev = newNode
        else:
            after = self.head.next
            newNode.prev = after.prev
            newNode.next = after
            self.head.next = newNode
            after.prev = newNode
        self.length += 1

    def pop(self) -> int:
        val = None
        if self.isEmpty():
            return -1
        if self.length == 1:
            val = self.head.next.val
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            val = self.tail.prev.val
            prev = self.tail.prev.prev
            prev.next = self.tail
            self.tail.prev = prev
        self.length -= 1
        return val

    def popleft(self) -> int:
        val = None
        if self.isEmpty():
            return -1
        if self.length == 1:
            val = self.head.next.val
            self.head.next = self.tail
            self.tail.prev = self.head
        else:
            val = self.head.next.val
            after = self.head.next.next
            after.prev = self.head
            self.head.next = after
        self.length -= 1
        return val
        
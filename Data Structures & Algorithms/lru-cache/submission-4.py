"""

capacity = 5

k: v
key: (value, Node)
hash map = {
    1: (1, 1),
    2: (2, 2),
    3: (3, 3),
    4: (4, 4),
    5: (5, 5),
}

class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

     = lru ----------------------------------------- mru
list = head <-> 1 <-> 2 <-> node <-> 4 <-> 5    <-> tail
list = head <-> 1 <-> 2 <->    4 <-> 5 <-> node <-> tail

"""
class Node:
    def __init__(self, key: int):
        self.key = key
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if self.size == 0:
            return -1

        elif key not in self.cache:
            return -1

        node = self.cache[key][1]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail
        
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        if self.get(key) != -1:
            self.cache[key][0] = value
        else:
            node = Node(key)
            self.cache[key] = [value, node]

            node.prev = self.tail.prev
            self.tail.prev.next = node
            node.next = self.tail
            self.tail.prev = node

            self.size += 1

        if self.size > self.capacity:
            to_remove = self.head.next.key

            tmp = self.head.next.next
            self.head.next = self.head.next.next
            tmp.prev = self.head

            if self.capacity == 1:
                self.tail.prev = tmp

            self.cache.pop(to_remove)
            self.size -= 1
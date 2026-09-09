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
        # print(f'initializing LRU cache with capacity: {capacity}')
        # initialize LRUCache data structures
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        # print()

    def get(self, key: int) -> int:
        # if cache is empty
        # print(f'attempting GET with key: {key}')
        if self.size == 0:
            # print(f'\tcache is empty, {key} not found')
            return -1

        # else if key not in cache
        elif key not in self.cache:
            # print(f'\tkey {key} not found')
            return -1

        # if key in cache
        # print(f'\tkey: {key} found, value: {self.cache[key][0]}')

        # find the node and mark it as used
        # head <-> 1 <-> tail
        # head <-> tail
        # head <-> 1 -> tail
        node = self.cache[key][1]
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
        node.next = self.tail
        
        # print()
        return self.cache[key][0]

    def put(self, key: int, value: int) -> None:
        # print(f'attempting PUT with key: {key}, value: {value}')
        if self.get(key) != -1:
            # print(f'\tkey: {key} found, replacing original value: {self.cache[key][0]} with {value}')
            self.cache[key][0] = value
        else:
            # print(f'\tkey: {key} not found. creating a new node and entry for key: {key}, value: {value}')
            node = Node(key)
            self.cache[key] = [value, node]

            # 2 <-> 3 <-> tail

            # head <-> 1 <-> 2 <-> tail

            node.prev = self.tail.prev
            self.tail.prev.next = node
            node.next = self.tail
            self.tail.prev = node

            self.size += 1

        if self.size > self.capacity:
            # print(f'\tsize {self.size} exceeds capacity {self.capacity}. removing LRU')
            to_remove = self.head.next.key
            # print(f'\tremoving key: {to_remove}')

            # head <-> 1 <-> tmp <-> tail
            # head <-> tmp <-> tail

            tmp = self.head.next.next
            self.head.next = self.head.next.next
            tmp.prev = self.head

            if self.capacity == 1:
                self.tail.prev = tmp

            self.cache.pop(to_remove)
            self.size -= 1

        # print('PUT successful')
        # print()
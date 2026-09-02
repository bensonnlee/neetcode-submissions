class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node(-1)
        self.length = 0
    
    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1
        
        cur = self.head.next
        for _ in range(index):
            cur = cur.next

        return cur.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        self.length += 1
        
    def remove(self, index: int) -> bool:
        if index > self.length - 1:
            return False
        prev = self.head
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
            prev = prev.next
        prev.next = cur.next
        self.length -= 1
        return True


    def getValues(self) -> List[int]:
        arr = []
        cur = self.head
        while cur.next:
            arr.append(cur.next.val)
            cur = cur.next
        return arr

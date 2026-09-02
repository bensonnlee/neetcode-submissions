class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.length = 0
    
    def get(self, index: int) -> int:
        if index > self.length - 1:
            return -1

        cur = self.head
        for i in range(index):
            cur = cur.next

        return cur.val

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insertTail(self, val: int) -> None:
        newNode = Node(val)

        if self.length == 0:
            self.head = newNode
        else:
            cur = self.head

            while cur.next:
                cur = cur.next

            cur.next = newNode
            # LL
            # 1 -> None

            # -> insertTail(2)

        self.length += 1

    def remove(self, index: int) -> bool:
        # if out of bounds
        if index > self.length - 1:
            return False
        
        # if size 1
        elif self.length == 1:
            self.head = None

        # if removing head
        elif index == 0:
            self.head = self.head.next

        # if removing tail
        elif index == self.length - 1:
            prev = self.head
            cur = self.head.next
            while cur.next:
                prev = prev.next
                cur = cur.next
            prev.next = None
        
        # if removing middle
        else:
            prev = self.head
            cur = self.head.next
            for _ in range(index - 1):
                prev = prev.next
                cur = cur.next
            prev.next = cur.next

        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        cur = self.head
        arr = []

        if not cur:
            return arr
        while cur:
            arr.append(cur.val)
            cur = cur.next

        return arr

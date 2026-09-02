class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        """
        dummy -> x -> y
        """
        self.head = Node(-1) # dummy pointer
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
        print(f'Inserting {val} to end of list: {self.getValues()}, length: {self.length}')
        newNode = Node(val)
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = newNode
        self.length += 1
        print(f'Inserted! List: {self.getValues()}, length: {self.length}')
        print()
        
    def remove(self, index: int) -> bool:
        # LL: dummy -> 1 -> 2
        # -> remove(1) -----^
        #              p    c 
        print(f'Removing index {index} from list: {self.getValues()}, length: {self.length}')
        if index > self.length - 1:
            print(f'Index out of bounds!')
            return False
        prev = self.head
        cur = self.head.next
        for _ in range(index):
            cur = cur.next
            prev = prev.next
        prev.next = cur.next
        self.length -= 1
        print(f'Removed! List: {self.getValues()}, length: {self.length}')
        print()
        return True


    def getValues(self) -> List[int]:
        arr = []
        cur = self.head
        while cur.next:
            arr.append(cur.next.val)
            cur = cur.next
        return arr

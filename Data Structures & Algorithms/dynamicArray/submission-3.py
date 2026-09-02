class DynamicArray:
    
    def __init__(self, capacity: int):
        print('init')
        self.size = 0
        self.capacity = capacity if capacity > 0 else 1
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.arr[self.getSize()] = n
        self.size += 1

    def popback(self) -> int:
        self.size -= 1
        return self.arr[self.getSize()]

    def resize(self) -> None:
        self.capacity *= 2
        self.arr.extend(self.arr)

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

"""
-> DynamicArray(1)
DynamicArray:
    size = 0
    capacity = 1
    arr = [0]

-> pushback(1)
DynamicArray:
    size = 1
    capacity = 1
    arr = [1]

-> pushback(2)
DynamicArray:
    size = 1
    capacity = 1
    arr = [1]
"""


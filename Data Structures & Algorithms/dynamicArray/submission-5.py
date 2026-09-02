class DynamicArray:
    
    def __init__(self, capacity: int):
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
        self.arr *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity

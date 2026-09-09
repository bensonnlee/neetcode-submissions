class MinStack:

    def __init__(self):
        self.min = []
        self.arr = []

    def push(self, val: int) -> None:
        if len(self.min) == 0 or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.arr.append(val)

    def pop(self) -> None:
        self.min.pop()
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min[-1]
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            heapq.heappush(self.heap, -num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        
        tmp = self.heap[:]
        for i in range(self.k - 1):
            heapq.heappop(tmp)
        return -heapq.heappop(tmp)
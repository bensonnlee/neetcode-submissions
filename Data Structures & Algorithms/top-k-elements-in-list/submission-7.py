class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most frequent
        # need counts of each number in nums
        count = {}  # k ->   v
                    # num -> freq

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # i want the k most frequent elements
        # min heap, remove items with least frequency
        heap = []

        # need to add all of these elements into the heap
        for key, value in count.items():

            # add the next item in
            heapq.heappush(heap, (value, key))

            # if length > k, remove smallest freq
            if len(heap) > k:
                heapq.heappop(heap)

        return [item[1] for item in heap]
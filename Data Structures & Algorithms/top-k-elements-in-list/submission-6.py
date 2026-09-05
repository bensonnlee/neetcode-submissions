class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # most frequent
        # need counts of each number in nums
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        """
        {
            3: 3
            2: 2
            1: 1
        }

        [ (1,5), (2,4), (3,3) ]
        """

        # sort the map, naive solution
        count_sorted = sorted(count.items(), reverse=True, key=lambda x: x[1])

        return [item[0] for item in count_sorted][:k]
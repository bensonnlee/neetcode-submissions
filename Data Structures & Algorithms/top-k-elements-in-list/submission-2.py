class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequencies of numbers
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        return sorted(count, key=lambda x: count[x], reverse=True)[:k]
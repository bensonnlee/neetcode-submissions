class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            ans[i] = sorted_count[i][0]
            
        return ans
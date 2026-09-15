class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

        arr = [[] for _ in range(len(nums) + 1)]
        for n, freq in counts.items():
            arr[freq].append(n)

        ans = []
        for subarr in reversed(arr):
            for num in subarr:
                if len(ans) == k:
                    continue
                ans.append(num)
        
        return ans
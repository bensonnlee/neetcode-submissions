class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts[n] = freq
        counts = {}
        for n in nums:
            counts[n] = 1 + counts.get(n, 0)

        # arr[frequency] = [numbers]
        arr = [[] for _ in range(len(nums) + 1)]
        for n, freq in counts.items():
            arr[freq].append(n)

        ans = []
        for subarr in reversed(arr):
            for num in subarr:
                if len(ans) == k:
                    return ans

                ans.append(num)

        return ans
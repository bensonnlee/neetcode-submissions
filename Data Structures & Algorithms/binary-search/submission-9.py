class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num == target:
                return idx
            
        return -1
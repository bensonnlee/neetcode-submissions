class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        idx = 0
        record = 1
        current = 1

        while idx < len(nums) - 1:
            if nums[idx] + 1 == nums[idx + 1]:
                current += 1
                record = max(current, record)
            elif nums[idx] == nums[idx + 1]:
                pass
            else:
                current = 1
            idx += 1

        return record
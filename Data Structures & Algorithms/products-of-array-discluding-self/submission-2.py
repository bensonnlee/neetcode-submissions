class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        prefix[0] = nums[0]
        suffix[-1] = nums[-1]

        # nums =    [1, 2,   3,   4, 5]
        # prefix =  [1, 2,   6,  24, 120]
        # suffix =  [0, 120, 60, 20, 5]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i]

        for i in range(len(nums) - 1, 0, -1):
            suffix[i - 1] = suffix[i] * nums[i - 1]

        ans = [0] * len(nums)
        ans[0] = suffix[1]
        ans[-1] = prefix[len(nums) - 2]
        for i in range(1, len(nums) - 1):
            ans[i] = prefix[i - 1] * suffix[i + 1]
        return ans
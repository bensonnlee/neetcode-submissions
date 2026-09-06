class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {} # s[num]: idx

        """
        nums = [3,4,5,6]
        target = 7
        i = 0

        diff = 4
        s = {}

        """

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in s:
                return [s[diff], i]
            s[nums[i]] = i
        
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        constraints:
            cannot rob two adjacent indices
            maximize money
            nums[i] = money at index
        """

        if len(nums) == 1:
            return nums[0]
        
        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(first + nums[i], second)
            first = second
            second = cur
    
        return second
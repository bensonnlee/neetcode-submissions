class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        constraints:
            cannot rob two adjacent indices
            maximize money
            nums[i] = money at index

        ---
        nums =  2
                9
                8
                3
                6

        dp   =  2
        """

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(
            nums[1], nums[0]
        )

        for i in range(2, len(nums)):
            first_choice = nums[i] + dp[i - 2]
            second_choice = dp[i - 1]
            dp[i] = max(first_choice, second_choice)

        return max(dp[-1], dp[-2])
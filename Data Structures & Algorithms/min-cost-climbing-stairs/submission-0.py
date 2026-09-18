class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        start on index 0 or index 1
        cost = [1]          -> 1
        dp   = [1]

        cost = [1, 2]       -> 1
        dp   = [1, 2]

        cost = [1, 2, 3]    -> 2
        dp   = [1, 2, 4]

        cost = [1, 2, 3, 4] -> 4
        dp   = [1, 2, 4, 6]

        """
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
    
        return min(dp[-2], dp[-1])
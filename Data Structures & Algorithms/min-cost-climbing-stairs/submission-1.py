class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        prevprev prev cur
        """
        prevprev = cost[0]
        prev = cost[1]

        for i in range(2, len(cost)):
            cur = cost[i] + min(prevprev, prev)

            prevprev = prev
            prev = cur

        return min(prev, prevprev)
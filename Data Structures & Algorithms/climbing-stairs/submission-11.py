class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0, 1, 2]
        #  0  1  2  3  4  5
        # [0, 1, 2, 3, 5, 8]
        
        if n < 3:
            return memo[n]

        for i in range(2, n):
            memo.append(memo[i-1] + memo[i])

        return memo[-1]
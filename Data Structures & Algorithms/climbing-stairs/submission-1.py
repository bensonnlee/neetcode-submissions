class Solution:
    def climbStairs(self, n: int) -> int:
        """
        n = 0
        ans = 0

        n = 1
        ans = 1

        n = 2
        ans = 2

        n = 3
        ans = 3

        n = 4
        ans = 5
        1 or 2, add up to 4 with any combo
        """

        """
        fib seq; f(1) = 1; f(2) = 2; f(3) = f(1) + f(2); f(4) = f(3) + f(2)
        """

        ans = [0, 1, 2]
        if n == 1:
            return ans[1]
        if n == 2:
            return ans[2]

        while n > len(ans) - 1:
            ans.append(ans[-1] + ans[-2])

        return ans[-1]
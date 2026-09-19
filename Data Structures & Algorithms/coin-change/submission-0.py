class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        constraints:
            coins must add up to the amount
            if impossible, return -1
            the amount of coins must be as minimal as possible

        thoughts:
            bottom-up approach
        """
        change = [float('inf')] * (amount + 1)
        change[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    change[i] = min(change[i], 1 + change[i - c])
        
        return -1 if change[-1] == float('inf') else change[-1]
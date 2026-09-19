class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        change = [float('inf')] * (amount + 1)
        change[0] = 0

        for i in range(1, len(change)):
            for c in coins:
                if i - c >= 0:
                    change[i] = min(change[i], 1 + change[i - c])

        return change[-1] if change[-1] != float('inf') else -1
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l != r:
            # too big, move right pointer down
            if numbers[l] + numbers[r] > target:
                r -= 1

            # too small, move left pointer up
            if numbers[l] + numbers[r] < target:
                l += 1

            # if l == r, no answer found (GUARANTEED SOLUTION)
            # if l == r:
            #     return []

            # if numbers[l] + numbers[r] == target, return ans
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
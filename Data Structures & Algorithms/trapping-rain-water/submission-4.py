class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max = height[0]
        right_max = height[-1]
        water = 0
        while l < r:
            if left_max <= right_max:
                to_add = left_max - height[l]
                if to_add > 0:
                    water += to_add
                l += 1
                left_max = max(left_max, height[l])
            else:
                to_add = right_max - height[r]
                if to_add > 0:
                    water += to_add
                r -= 1
                right_max = max(right_max, height[r])
        return water
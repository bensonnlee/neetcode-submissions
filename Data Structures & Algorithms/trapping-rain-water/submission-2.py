class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        highest_l = [0] * len(height)
        highest_r = [0] * len(height)

        highest = 0
        for i in range(len(height)):
            highest = max(highest, height[i])
            highest_l[i] = highest
        
        highest = 0
        for i in range(len(height) - 1, -1, -1):
            highest = max(highest, height[i])
            highest_r[i] = highest

        for height_i, left_height, right_height in zip(height, highest_l, highest_r):
            to_add = min(left_height, right_height) - height_i
            if to_add > 0:
                water += to_add

        return water

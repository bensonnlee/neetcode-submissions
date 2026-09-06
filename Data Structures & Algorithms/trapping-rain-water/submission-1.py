class Solution:
    def trap(self, height: List[int]) -> int:
        """
        precompute the height of the leftmost and the rightmost


        create a precomputed array at each height with the
        tallest thing on the left and right of the current index
        """
        water = 0
        highest_l = [0] * len(height)
        highest_r = [0] * len(height)

        highest = 0
        for i in range(len(height)):
            highest = max(highest, height[i])
            highest_l[i] = highest
        
        highest = 0
        for i in range(len(height) - 1, 0, -1):
            highest = max(highest, height[i])
            highest_r[i] = highest

        """
        height= [0,2,0,3,1,0,1,3,2,1]
        l=      [0,2,2,3,3,3,3,3,3,3]
        r=      [3,3,3,3,3,3,3,3,2,1]
        """

        for height_i, left_height, right_height in zip(height, highest_l, highest_r):
            to_add = min(left_height, right_height) - height_i
            if to_add > 0:
                water += to_add


        return water
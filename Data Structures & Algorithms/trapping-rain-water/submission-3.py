class Solution:
    def trap(self, height: List[int]) -> int:
        l = [0 , height[0]]
        r = [len(height) - 1, height[-1]]
        water = 0
        while l[0] < r[0]:
            if l[1] <= r[1]:
                to_add = l[1] - height[l[0]]
                if to_add > 0:
                    water += to_add
                l[0] += 1
                l[1] = max(l[1], height[l[0]])
            else:
                to_add = r[1] - height[r[0]]
                if to_add > 0:
                    water += to_add
                r[0] -= 1
                r[1] = max(r[1], height[r[0]])
        return water
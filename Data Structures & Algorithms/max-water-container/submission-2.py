class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        want an area helper function?

        brute force: go through all of the heights and
                     store the max amount of water
                     time complexity: O(n^2)
                     space complexity: O(1)
        """
        def _get_area_between(l: int, r: int) -> int:
            width = r - l
            height = min(heights[l], heights[r])
            return width * height

        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if _get_area_between(l, r) > max_area:
                max_area = _get_area_between(l, r)
            else:
                if heights[l] < heights[r]:
                    l += 1
                else:
                    r -= 1

        return max_area
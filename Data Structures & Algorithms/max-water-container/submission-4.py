class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def _get_area_between(l: int, r: int) -> int:
            width = r - l
            height = min(heights[l], heights[r])
            return width * height

        max_area = 0
        l, r = 0, len(heights) - 1
        while l < r:
            if _get_area_between(l, r) > max_area:
                max_area = _get_area_between(l, r)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return max_area
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, ocean, prev):
            if (
                (r, c) in ocean or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                heights[r][c] < prev
            ):
                return

            ocean.add((r, c))
            for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                dfs(r + dr, c + dc, ocean, heights[r][c])

        # pacific
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
        
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
        
        # atlantic
        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        return [list(p) for p in atlantic & pacific]
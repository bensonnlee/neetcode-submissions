class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        visited = set()
        max_area = 0

        def dfs(r, c):
            # if out of bounds
            if not 0 <= r < ROWS or not 0 <= c < COLS or (r, c) in visited or grid[r][c] == 0:
                return 0
            
            count = 0

            visited.add((r, c))

            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count + 1

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))

        return max_area
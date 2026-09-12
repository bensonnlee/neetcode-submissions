class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        max_area = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = 0
            area = 0
            while q:
                r, c = q.popleft()
                area += 1
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 0
                        q.append((nr, nc))
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    max_area = max(max_area, bfs(r, c))

        return max_area
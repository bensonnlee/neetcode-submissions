class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        treasure = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    treasure.add((r, c))

        queue = deque()
        for r, c in treasure:
            queue.append((r, c))

        level = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = level
                        queue.append((nr, nc))
                    else:
                        continue
            level += 1  
    
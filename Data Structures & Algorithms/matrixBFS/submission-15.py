class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visited = set()
        queue = deque()
        queue.append((0, 0))

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [
                    [0, 1], [0, -1], [1, 0], [-1, 0]
                ]
                
                for dr, dc in neighbors:
                    if (
                        min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        grid[r + dr][c + dc] == 1 or
                        (r + dr, c + dc) in visited
                    ):
                        continue
                    
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            length += 1

        return -1
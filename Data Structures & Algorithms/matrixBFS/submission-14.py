class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()

        if grid[0][0] == 0:
            visited.add((0, 0))
            queue.append((0, 0))
        else:
            return -1

        if ROWS == 0:
            return -1

        length = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    # if neighbor not eligible, skip
                    if (
                        min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visited or
                        grid[r + dr][c + dc] == 1
                    ):
                        continue
                    
                    # otherwise, add neighbor to queue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            # processed all of the nodes in the depth, proceed to next depth
            length += 1

        return -1
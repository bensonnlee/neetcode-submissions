class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        # early exit; no possible paths
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        visited = set()
        queue = deque()
        
        # add start to the queue
        queue.append((0, 0))

        length = 0

        # while there's still nodes to process
        while queue:
            # process the entire depth
            for _ in range(len(queue)):
                r, c = queue.popleft()

                # if at the end, done!
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                # all potentially possible paths
                neighbors = [
                    [0, 1], [0, -1], [1, 0], [-1, 0]
                ]
                
                for dr, dc in neighbors:
                    # if non eligible to traverse, skip
                    if (
                        min(r + dr, c + dc) < 0 or
                        r + dr == ROWS or c + dc == COLS or
                        grid[r + dr][c + dc] == 1 or
                        (r + dr, c + dc) in visited
                    ):
                        continue
                    
                    # add to queue and visited list
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))

            # after processing the entire depth, increase length
            length += 1

        return -1
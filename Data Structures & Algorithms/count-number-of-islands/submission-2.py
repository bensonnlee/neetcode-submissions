class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        go through all of the nodes, add node to visited set

        if node is a 1:
            do dfs/bfs on that node,
            add all visited nodes to visited set
            add 1 to num_islands when done
        
        continue until no more nodes
        """
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    num_islands += 1

        return num_islands
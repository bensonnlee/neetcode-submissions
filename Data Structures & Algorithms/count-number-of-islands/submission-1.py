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

        def dfs(r, c):
            if (
                min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r, c) in visited or
                grid[r][c] == "0"
            ):
                return

            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        num_islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c)
                    num_islands += 1

        return num_islands
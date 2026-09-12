class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        pacific = set()

        atlantic = set()

        """
        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def bfs(r, c, ocean):
            queue = deque([(r, c)])
            ocean.add((r, c))
            
            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    for dr, dc in ((-1,0),(1,0),(0,1),(0,-1)):
                        nr, nc = r + dr, c + dc

                        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in ocean and heights[nr][nc] >= heights[r][c]:
                            ocean.add((nr, nc))
                            queue.append((nr, nc))


        # pacific traversal
        for c in range(COLS):
            bfs(0, c, pacific)
        
        for r in range(ROWS):
            bfs(r, 0, pacific)

        # atlantic traversal
        for c in range(COLS):
            bfs(ROWS - 1, c, atlantic)

        for r in range(ROWS):
            bfs(r, COLS - 1, atlantic)

        ans = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append((r, c))
        return ans
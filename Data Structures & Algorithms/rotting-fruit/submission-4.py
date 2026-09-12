class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        fresh = set()
        rotten = set()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh.add((r, c))
                if grid[r][c] == 2:
                    rotten.add((r, c))

        time = 0

        while fresh:
            to_add = set()
            for r, c in rotten:
                for dr, dc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if (dr, dc) in fresh:
                        fresh.remove((dr, dc))
                        to_add.add((dr, dc))
            time += 1

            if not to_add:
                return -1

            rotten = to_add

        return time
    
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0
        def dfs(r, c, visit):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == '0':
                return
            visit.add((r,c))
            dfs(r + 1, c, visit) # where- right
            dfs(r - 1, c, visit)# left
            dfs(r, c + 1, visit) # up
            dfs(r, c - 1, visit) # down
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r, c, visit)
                    res += 1
        print(res)
        return res
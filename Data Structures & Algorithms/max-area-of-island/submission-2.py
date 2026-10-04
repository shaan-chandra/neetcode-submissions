class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        visit = set()
        # dfs should just calculate area
        def dfs(r, c, visit, count):
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit:
                return 0
            visit.add((r,c))
            #print("count: ", count)
            right = dfs(r + 1, c, visit, count)
            left = dfs(r - 1, c, visit, count) 
            up = dfs(r, c + 1, visit, count) 
            down = dfs(r, c - 1, visit, count) 
            return 1 + right + left + up + down

        for r in range(rows):
            count = 0
            for c in range(cols):
                #print("grid: ", grid[r][c])
                if grid[r][c] == 1 and (r,c) not in visit:
                    #print('is dfs working?: ', grid[r][c])
                    count = dfs(r,c,visit,count)
                    #print("count we got", tmp)
                    res = max(res, count)
                    #print("res: ", res)
        print(res)
        return res
                

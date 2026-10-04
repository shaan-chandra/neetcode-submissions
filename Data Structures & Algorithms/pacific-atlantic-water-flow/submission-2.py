class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # just run it from each cell where pacific starts and track where pacific meets atlantic and vice versa but if a path can reach from pacific to atlantic it can also reach atlantic to pacific right
        res = []
        rows, cols = len(heights), len(heights[0])
        visit_p, visit_a = set(), set()

        def dfs(parent,r,c,visit):
            if r not in range(rows) or c not in range(cols) or heights[r][c] < parent or (r,c) in visit:
                return  
                # water successfully reached the target (atlantic or pacific)
            visit.add((r,c))
            dfs(heights[r][c], r + 1, c, visit)
            dfs(heights[r][c], r - 1, c, visit)
            dfs(heights[r][c], r, c + 1, visit)
            dfs(heights[r][c], r, c - 1, visit)
        
        # run dfs from pacific 
        for r in range(rows):
            dfs(heights[r][0], r, 0, visit_p)
            dfs(heights[r][cols - 1], r, cols - 1, visit_a)
        for c in range(cols):
            # run once from pacific and run once from atlantic store both
            dfs(heights[0][c], 0, c, visit_p,)
            dfs(heights[rows - 1][c], rows - 1, c, visit_a)
        #print("pacific: ", visit_p)
        #print("atlantic: ", visit_a)
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in visit_p and (r,c) in visit_a:
                    res.append((r,c))
        #print(res)
        return res

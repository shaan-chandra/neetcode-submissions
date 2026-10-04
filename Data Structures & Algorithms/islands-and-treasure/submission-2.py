class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def bfs(r, c, visit):
            if r not in range(rows) or c not in range(cols) or ((r,c)) in visit or grid[r][c] == -1:
                return 
            visit.add((r,c))
            q.append((r,c))

        # 1) add all treasure chests to q
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visit.add((r,c))
                    q.append((r,c))
        #print(q)
        # perfect now- logic just run dfs frmo the sources 
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                # helper to add items to bfs q
                bfs(r + 1, c, visit)
                bfs(r - 1, c, visit)
                bfs(r, c + 1, visit)
                bfs(r, c - 1, visit)
            dist += 1
        #print(grid)

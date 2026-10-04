class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        # easy same as dist but just after each min just check its neighbours 
        visit = set()
        # multi source bfs 
        q = deque()
        fresh = 0
        rows, cols = len(grid), len(grid[0])

        # first add rotten fruits to set 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
                    visit.add((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        def bfs(r, c, visit):
            nonlocal fresh
            if r not in range(rows) or c not in range(cols) or grid[r][c] == 0 or (r,c) in visit:
                return 
            visit.add((r,c))
            q.append((r,c))
            fresh -= 1
            #print('fresh update: ', fresh)
            
        while fresh > 0 and q:
            #print(q)
            for i in range(len(q)):
                #print("time of rotten: ", time)
                r, c = q.popleft()
                #print(r,c)
                grid[r][c] = 2

                bfs(r + 1, c, visit)
                bfs(r - 1, c, visit)
                bfs(r, c + 1, visit)
                bfs(r, c - 1, visit)
            time += 1 if q else 0
        #print(time)
        #print(fresh)
        return time if fresh == 0 else -1
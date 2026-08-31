class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        res = 0
        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)
        # keep dfs only to track nodes visited
        visit = set()
        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adjList[node]:
                dfs(nei)

        for node in range(n):
            if node not in visit:
                dfs(node)
                res += 1
        return res
            
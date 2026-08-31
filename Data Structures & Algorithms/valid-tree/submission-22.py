class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True 
        adjList = defaultdict(list)
        visit = set()
        for node, edge in edges:
            adjList[node].append(edge)
            adjList[edge].append(node)
        def dfs(node, prev):
            if node in visit:
                return False 
            visit.add(node)
            for nei in adjList[node]:
                if nei == prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visit)
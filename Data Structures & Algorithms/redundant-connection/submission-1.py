class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        # better to make visit
        #print(adjList)
        # run dfs to 
        def dfs(node, parent, visit):
            if node in visit:
                return True 
            visit.add(node)
            for nei in adjList[node]:
                if nei == parent:
                    continue 
                if dfs(nei, node, visit):
                    return True 
            return False 
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
            if dfs(u, -1, set()):
                return [u,v]
        return [] 
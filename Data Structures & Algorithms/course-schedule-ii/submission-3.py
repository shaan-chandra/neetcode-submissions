class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort its easy 
        adjList = defaultdict(list)
        visit = set()
        node_seen = set()
        res = []
        for node, edge in prerequisites: 
            adjList[node].append(edge)
        def dfs(node):
            if node in node_seen:
                return False 
            if node in visit:
                return True
            node_seen.add(node)
            for nei in adjList[node]:
                if not dfs(nei):
                    return False
            node_seen.remove(node)
            visit.add(node)
            res.append(node)
            return True
        for courses in range(numCourses):
            if not dfs(courses):
                return []
        return res 
        

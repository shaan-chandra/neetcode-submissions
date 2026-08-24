class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        visit = set()
        # before dfs i gotta build adjList 
        for node, edge in prerequisites:
            adjList[node].append(edge)
        print(adjList)
        def dfs(node):
            if node in visit:
                return False
            visit.add(node) 
            for nei in adjList[node]:
                if not dfs(nei): return False
            visit.remove(node)
            adjList[node] = []
            return True 
        for courses in range(numCourses):
            if not dfs(courses): return False 
        return True
            
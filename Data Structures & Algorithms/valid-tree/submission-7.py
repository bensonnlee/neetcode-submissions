class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = [[] for _ in range(n)]

        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        seen = set()
        def dfs(node, parent):
            if node in seen:
                return False

            seen.add(node)
            for neighbor in adjList[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False

            return True
        
        return dfs(0, -1) and len(seen) == n
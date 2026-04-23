class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        #make adj list
        adj_list = [[] for _ in range(n)]

        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        #print(adj_list)

        visited = set()

        def dfs(node):
            #if current node is already visited return False
            if node in visited:
                return

            #add node to visisted
            visited.add(node)

            #dfs all neighbors
            for neighbor in adj_list[node]:
                dfs(neighbor)

        
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components
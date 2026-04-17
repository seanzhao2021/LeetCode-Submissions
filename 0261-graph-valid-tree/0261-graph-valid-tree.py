class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """

        adj_list = [[] for _ in range(n)] 

        for i in range(len(edges)):
            adj_list[edges[i][0]].append(edges[i][1])
            adj_list[edges[i][1]].append(edges[i][0])

        visited = set()

        def dfs(node, parent):
            #add to visited
            visited.add(node)

            #for every child
            for child in adj_list[node]:
                #is this my parent?
                    #skip this child
                if child == parent:
                    continue
                #is this in visited?
                    #cycle detected
                if child in visited:
                    return False
                
                #dfs(child)
                if not dfs(child, node):
                    return False

            return True

        
        
        return dfs(0,None) and len(visited) == n
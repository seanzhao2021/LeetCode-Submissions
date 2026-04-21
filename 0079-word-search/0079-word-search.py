class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()
        def dfs(i, j, idx):
            #if i or j out of bounds
            if i >= len(board) or i < 0:
                return False
            if j >= len(board[0]) or j < 0:
                return False
            
            #if node is visited
            #if (i, j) in visited:
            if board[i][j] == "#":
                return False
            
            #if idx got to the very end
            if idx == len(word) - 1 and board[i][j] == word[idx]:
                return True
            
            #is current letter matching with word
            if board[i][j] != word[idx]:
                return False

            #add node to visited
            #visited.add((i, j))
            temp = board[i][j]
            board[i][j] = "#"

            #dfs all neighbors
            #if dfs or dfs or dfs or dfs
            if dfs(i + 1, j, idx + 1) or dfs(i - 1, j, idx + 1) or dfs(i, j + 1, idx + 1) or dfs(i, j - 1, idx + 1):
                return True

            #pop node from visited
            #visited.remove((i, j))
            board[i][j] = temp

            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True
        return False
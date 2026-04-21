class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        ROW = len(board)
        COL = len(board[0])
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
        
        first_cnt = 0
        last_cnt = 0
        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == word[0]: first_cnt += 1
                if board[i][j] == word[-1] : last_cnt += 1
        
        #lets reverse string is last letter is rarer than first letter
        if last_cnt < first_cnt:
            word[::-1]

        for i in range(ROW):
            for j in range(COL):
                if dfs(i, j, 0):
                    return True
        return False
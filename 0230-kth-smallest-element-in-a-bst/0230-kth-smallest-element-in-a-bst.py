# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.i = 0
        #in order traversal
        #left - root - right
        def dfs(root):
            #base case
            #node we are at is none
            if not root:
                return None

            #dfs left
            left = dfs(root.left)
            if left is not None:
                return left

            self.i += 1
            #check if i == k
            #then this node we are on is the answer
            if self.i == k:
                return root.val

            #dfs right
            right = dfs(root.right)
            if right is not None:
                return right


        return dfs(root)
        
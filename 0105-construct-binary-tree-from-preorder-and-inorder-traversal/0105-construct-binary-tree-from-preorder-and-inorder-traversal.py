# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        
        #divide and conquer
        #find left and right subtrees from root
        #root.left = left subtree and .right = right subtree
        #recursively build subtrees and roots

        #first element of inorder traversal is the root
        #traverse preorder until we find the root
            #everything to the left of that root in preorder is the left side of the tree
            #everything to the right is the right side of the tree
        #recursively build subtrees

        self.i = 0

        ht = {}
        for i in range(len(inorder)):
             ht[inorder[i]] = i

        def dac(l, r):
            #baes case
            if l > r:
                return None
            
            target = preorder[self.i]
            self.i += 1

            root = TreeNode(target)

            pos = ht[target]

            #left
            root.left = dac(l, pos - 1)
            #right
            root.right = dac (pos + 1, r)

            return root
        
        return dac(0, len(inorder) - 1)
        
        # def dac(inorder):
        #     #base case
        #     #only one element in arr
        #     if len(inorder) == 1:
        #         #return tree node of that element
        #         #somehow need to popleft from preorder
        #         self.i += 1
        #         # print(inorder)
        #         return TreeNode(inorder[0])

        #     #first find root?
        #     target = preorder[self.i]
        #     idx = 0

        #     # print(self.i)
        #     # print(inorder)
        #     # print(idx, target)
        #     #print(preorder)

        #     while inorder[idx] != target:
        #         idx += 1

        #     #after we found root
        #     leftTree, rightTree = None, None
        #     self.i += 1
        #     #root has values on left
        #     if idx != 0:
        #         #popleft preorder arr
        #         leftTree = dac(inorder[0:idx])

        #     #root has values on right
        #     if idx != len(inorder) - 1:
        #         #popleft preorder arr
        #         rightTree = dac(inorder[idx+1:])

        #     ####
        #     return TreeNode(target, leftTree, rightTree)
        
        # return dac(inorder)

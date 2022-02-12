# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## Refer to https://velog.io/@lucid/LeetCode-101.-Symmetric-Tree
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        
        def isSymmetricSub(left, right):
            ## when both left and right node is None, it is symmetric
            if left == None and right == None:
                return True

            ## when only one side of node is None, it is asymmetric
            if (left != None and right == None) or (left == None and right != None):
                return False

            ## when left and right node value is different, it is asymmetric
            if left.val != right.val:
                return False
            return isSymmetricSub(left.left, right.right) and isSymmetricSub(left.right, right.left)

        return isSymmetricSub(root.left, root.right)


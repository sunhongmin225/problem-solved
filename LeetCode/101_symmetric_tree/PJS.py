# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# I freeze up when I encounter trees and did so this time....
# Definitely need more practice : (
# the solution here is referenced from https://velog.io/@lucid/LeetCode-101.-Symmetric-Tree

class Solution:
    def symmetricLR(self, left, right):
        if left is None and right is None:
            return True
        if (left is None and right is not None) or \
            (left is not None and right is None):
            return False
        if left.val != right.val:
            return False
        
        return self.symmetricLR(left.left, right.right) and \
                self.symmetricLR(left.right, right.left)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.symmetricLR(root.left, root.right)

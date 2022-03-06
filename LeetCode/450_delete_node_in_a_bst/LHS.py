# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Refer to https://velog.io/@timevoyage/leetcode-450
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        # find the min val in right side tree
        def minNext(node):
            while node.left != None:
                node = node.left
            return node
        
        # empty tree case
        if root == None:
            return root
        
        # key is in the right tree
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        # key is in the left tree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        # key is same as val
        else:
            if root.left == None:
                return root.right
            if root.right == None:
                return root.left
            minNode = minNext(root.right)
            root.val = minNode.val
            root.right = self.deleteNode(root.right, root.val)
        return root

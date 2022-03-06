# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            def findNext(node):
                while node.left is not None:
                    node = node.left
                return node
            
            # find the next larger node (leftmost of the right subtree)
            next_node = findNext(root.right)
            # change root value to the next larger node
            root.val = next_node.val
            # remove that next larger node from the right subtree
            root.right = self.deleteNode(root.right, next_node.val)
        
        return root

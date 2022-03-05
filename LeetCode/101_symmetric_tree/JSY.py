'''
1. Should work more with problems on tree DS
2. Referred to https://june-coder.tistory.com/15 
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSubtreeSymmetric(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            else:
                return left.val == right.val and isSubtreeSymmetric(left.left, right.right) and isSubtreeSymmetric(left.right, right.left)      
            
        return isSubtreeSymmetric(root, root)
        


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    def subpathSum(self, root, targetSum):
        if root.left is None and root.right is None:
            if root.val == targetSum:
                self.count += 1
            return [root.val]
        
        ret = []
        ret.append(root.val)
        if root.left:
            llist = self.subpathSum(root.left, targetSum)
            lsum = [x+root.val for x in llist]
            ret.extend(lsum)
        if root.right:
            rlist = self.subpathSum(root.right, targetSum)
            rsum = [x+root.val for x in rlist]
            ret.extend(rsum)
        self.count += ret.count(targetSum)
        return ret
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.subpathSum(root, targetSum)
        return self.count

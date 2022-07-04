# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#referred to https://lessbutbetter.tistory.com/entry/LeetCodeMediumC%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-437-Path-Sum-III
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        # dfs: returning the number of paths for targetSum including the root.
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    
    def dfs(self, root, targetSum):
        if root is None: 
            return 0
        else:
            return int(root.val == targetSum) + self.dfs(root.left, targetSum - root.val) + self.dfs(root.right, targetSum - root.val)

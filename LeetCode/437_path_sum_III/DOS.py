class Solution:

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.numPaths = 0
        self.get_path_sum(root,[],targetSum)
        return self.numPaths

    def get_path_sum(self, root,path,targetSum):
        if root is None:
            return
        path.append(root.val)
        self.get_path_sum(root.left,path,targetSum)
        self.get_path_sum(root.right,path,targetSum)
        _sum = 0
        for i in range(len(path)-1,-1,-1):
            _sum += path[i]
            if _sum == targetSum:
                self.numPaths += 1
        path.pop()


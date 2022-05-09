# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth = 0
        self.findDepth(root, 0)
        # print(f"depth: {self.depth}")
        node_num = 2**(self.depth+1) - 1
        # print(f"node num: {node_num}")
        self.cnt = 0
        queue = []
        queue.append(root)
        total_order = []
        while queue:
            temp = queue.pop(0)
            self.cnt +=1
            if self.cnt == node_num+1:
                break
            # print(temp.val)
            total_order.append(temp.val)
            if temp.left is not None:
                queue.append(temp.left)
            else:
                temp.left = TreeNode(200)
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)
            else:
                temp.right = TreeNode(200)
                queue.append(temp.right)
        # print(total_order)
        max_width = 0
        for i in range(self.depth+1):
            if i == 0 and total_order[0]!=200:
                max_width = 1
                continue
            st = 2**i -1
            end = 2**(i+1)-1
            # print(total_order[st:end])
            val_list= []
            for j in range(st, end):
                if total_order[j] != 200:
                    val_list.append(j)
            
            # print(val_list)
            # print(max(val_list)-min(val_list)+1)
            max_width = max(max_width, max(val_list)-min(val_list)+1)
        return max_width    
            
    def findDepth(self, root, depth):
        if root.left is not None:
            self.findDepth(root.left, depth+1)
            self.depth = max(self.depth, depth+1)
        if root.right is not None:
            self.findDepth(root.right, depth+1)
            self.depth = max(self.depth, depth+1)

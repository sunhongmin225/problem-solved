# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# time limit exceed...
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # max depth for total count
		self.depth = 0
        self.findDepth(root, 0)
        
		# total number of nodes
		node_num = 2**(self.depth+1) - 1
        self.cnt = 0
        queue = []
        queue.append(root)
        total_order = []
        while queue:
            temp = queue.pop(0)
            self.cnt +=1
	        # if the number of nodes if full, break    
			if self.cnt == node_num+1:
                break
            total_order.append(temp.val)
            
			# if left or right node is not null, add it to queue
			# if is null, create node with value=200
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

		# find max_width by iterating level
        max_width = 0
        for i in range(self.depth+1):
            if i == 0 and total_order[0]!=200:
                max_width = 1
                continue
            st = 2**i -1
            end = 2**(i+1)-1
            val_list= []
            for j in range(st, end):
                if total_order[j] != 200:
                    val_list.append(j)
            max_width = max(max_width, max(val_list)-min(val_list)+1)
        return max_width    
            
    def findDepth(self, root, depth):
        if root.left is not None:
            self.findDepth(root.left, depth+1)
            self.depth = max(self.depth, depth+1)
        if root.right is not None:
            self.findDepth(root.right, depth+1)
            self.depth = max(self.depth, depth+1)

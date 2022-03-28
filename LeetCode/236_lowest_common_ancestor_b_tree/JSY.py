# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p_ancestors = [p]
        q_ancestors = [q]
        
        # self.find(root, p, p_ancestors)
        self.find(root, q, q_ancestors)
        # print("here")
        # print(p_ancestors)
        print(q_ancestors)
        # find what's common in p_ancestors and q_ancestors starting from left to right
        common = set(p_ancestors) - (set(p_ancestors) - set(q_ancestors))
        return list(common)[0]
        
    def find(self, node: 'TreeNode', target: 'TreeNode', ancestors: List['TreeNode']):
        print(node.val)
        if node.left == node.right == None and node.val != target.val:
            return False
        elif node.val == target.val: 
            print("true")
            print(node.val)
            return True

        if self.find(node.left, target, ancestors):
            print(node.left.val)
            ancestors.append(node)
            return True

        if self.find(node.right, target, ancestors):
            print(node.right.val)
            ancestors.append(node)
            return True
 
        return ancestors
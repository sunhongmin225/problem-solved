# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# reference: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=1ilsang&logNo=221603869786

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None

        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q);
        right = self.lowestCommonAncestor(root.right, p, q);

        # left & right are not None if they contain p or q

        if left is not None and right is not None:
            # p, and q each are in either left or right subtree
            return root

        if left is not None:
            # both p and q are in left subtree
            return left
        else:
            # both p and q are in right subtree
            return right
        
        """
        # When I thought this was a binary search tree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            # when 'root'is the diverging point for p & q
            return root
        """

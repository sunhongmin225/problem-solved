# Refer to https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=1ilsang&logNo=221603869786
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if(root is None or root == q or root == p):
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if(left is None):
            return right
        elif(right is None):
            return left
        else:
            return root

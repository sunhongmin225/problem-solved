# subscribed to leetcode premium so no need to debug from local env

class Solution:
    def isSymmetric(self, root) -> bool:
        lt, rt = root.left, root.right
        return is_same(lt, rt)

def is_same(lt, rt):
    # base case
    if lt is None and rt is None: return True
    if lt is None or rt is None: return False
    
    # recursion
    if lt.val == rt.val:
        return is_same(lt.right, rt.left) and is_same(lt.left, rt.right)
    return False
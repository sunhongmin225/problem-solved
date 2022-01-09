import math

class Solution:
    def reverse(self, x: int) -> int:
        is_neg = False
        if x < 0:
            x = x* -1
            is_neg = True
        
        # I found out that python considers longlong types as 'int'
        # and therefore this does not cause any exception...
        result = int(str(x)[::-1])
        
        if is_neg:
            result = -1 * result
        
        if (result < -1 * math.pow(2, 31)) or (result > math.pow(2, 31) - 1):
            return 0
        else:
            return result

class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        
        ## output format +/-
        if x >= 0:
            res = ''
        else:
            res ='-'
            
        ## serial zeros elimination
        div = x 
        while(div % 10 == 0):
            div /= 10
            div = int(div)
            
        while(div != 0):
            if x >= 0:
                res += str(div % 10)
            else:
                res += str(10 - (div % 10))[-1]
            div /= 10
            div = int(div)

        ## out of bound
        if int(res) >= 2**31:
            return 0
        if int(res) <= -2**31-1:
            return 0
        return res
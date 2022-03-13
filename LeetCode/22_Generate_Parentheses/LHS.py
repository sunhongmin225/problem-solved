class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ## initialize parenthesis string   
        par = "("
        left = 1
        right = 0

        ans = []
        
        def makePar(par, left, right):
            # if right is full, append string and return
            if right == n:
                ans.append(par)
                return
            # we can add parenthesis pair only if when left is bigger or equal to right
            if left > right:
                # when left is not full, we can add both "(" and ")"
                if left < n:
                    makePar(par+"(", left+1, right)
                    makePar(par+")", left, right+1)
                # when left is full, we can only add ")"
                elif left == n:
                    makePar(par+")", left, right+1)
            # if left and right is same, we can only add "("
            elif left == right:
                makePar(par+"(", left+1, right)
            
        makePar(par, left, right)
        return ans

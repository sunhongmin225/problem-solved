# noticed that I should solve this with backtracking, but it was difficult to code it...
# referred to https://m.blog.naver.com/babobigi/221478657966

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []
        self.backtracking(output, "", n, 0, 0)
        return output
    
    def backtracking(self, output, curr_str, n, num_open, num_closed):
        # keep track of the number of open / closed parenthesis
        
        if len(curr_str) == 2 * n:
            output.append(curr_str)
            return
        
        if num_closed < num_open:
            self.backtracking(output, curr_str + ')', n, num_open, num_closed + 1)
        
        if num_open < n:
            self.backtracking(output, curr_str + '(', n, num_open + 1, num_closed)

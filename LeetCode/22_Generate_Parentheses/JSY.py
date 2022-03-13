# Type: DFS
# 1. constraint가 작으면 recursion을 적용하는 걸 고려해보기. 
# 2. 다음번엔 backtrack 방식대로 다시 풀어보기.

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        left = right = n
        answers = []
        
        self.recursive(answers, '(', left - 1, right)
        return answers
        
        
    def recursive(self, answers: List[str], ans: str, left: int, right: int):
        if left == right == 0:
            answers.append(ans)
            return answers
            # return 
            # return answers 대신 return만 해도 answers의 값이 다 유지가 되는게 이해되지 않음...

        if left > 0:
            self.recursive(answers, ans + '(', left - 1, right)
        
        if left < right:
            self.recursive(answers, ans + ')', left, right - 1)





if __name__ == "__main__":
    n = 3
    print(Solution().generateParenthesis(n))
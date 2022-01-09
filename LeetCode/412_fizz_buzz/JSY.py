# Retrospect
# 1. 잔실수

class Solution:
    def fizzBuzz(self, n: int):
        # initialize with None
        ans = [None] * n 

        for i, val in enumerate(ans):
            tar = i + 1
            if tar % 3 == 0:
                if tar % 5 == 0: # 15의 배수
                    ans[i] = "FizzBuzz"
                else: # NOTE: 실수로 분기를 뺌. 
                    ans[i] = "Fizz"
            elif tar % 5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(tar)
        
        for item in ans:
            assert item != None

        return ans            



if __name__ == "__main__":
    solution = Solution()
    INT = 10000

    print(solution.fizzBuzz(INT))
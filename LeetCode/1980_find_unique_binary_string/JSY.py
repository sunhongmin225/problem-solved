# TYPE: implementation

# Retrospect
# 1. base 10을 쓰는 방법 말고 recursion도 쓸 수 있을 거 같음. recursion도 연습해보자. 
# 2. map 함수 문법 실수하지 말기. map(함수, iterable)
# 3. 이진법 <-> 십진법 변환 방법 모름. 몰라도 되긴 하는데, 알아두자면 int(binary 숫자, 2)
# 4. python set is not subscriptable. subscriptable하게 만드려면 list로 바꿀 것. 
# 5. (정말 잊지 말아야할 것) 나누기하면 결과가 float으로 나온다. 몫을 구하고자 한다면 int로 캐스팅해야함.

import typing
from typing import List

class Solution:
    def ten_to_str_bin(self, num: int, digit: int) -> str:
        ans = ""
        for i in range(digit):
            mok = int(num / 2)
            namuji = num % 2
            ans = str(namuji) + ans
            
            if mok == 0:
                ans = (digit - len(ans))*"0" + ans
                break
            else:
                num = mok

        assert len(ans) == digit

        return ans

    def str_bin_to_ten(self, num: str, digit: int) -> int:
        sum = 0
        for i in range(digit): 
            sum += int(num[digit-1-i])*(2**i)
        
        return sum

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # 1. switch strings in the list to base 10
        digit = len(nums[0])
        nums = [self.str_bin_to_ten(num, digit) for num in nums] # bin -> tens
        
        # 2. enumerate all the possible nums and get the missing nums
        total = [i for i in range(2**digit)]
        remaining = set(total) - set(nums)

        # 3. take any number in remaining and convert it to bin
        ans = list(remaining)[-1] # took the LAST number in remaining
        ans = self.ten_to_str_bin(ans, digit)

        return ans

        
if __name__ == "__main__":
    # nums = ["00", "10"]
    # nums = ["00", "01"]
    nums = ["111", "011", "001"]
    
    print(Solution().findDifferentBinaryString(nums))
    # print(Solution().ten_to_str_bin(6, 3))
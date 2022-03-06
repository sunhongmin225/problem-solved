'''
이게 sorting 문제라고 생각하지 못했음. 
sorting 문제를 좀 더 풀어야 할 거 같음
Referred to: https://velog.io/@pyh8618/LeetCode-179.-Largest-Number 

'''

from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def check_swap(a: int, b: int) -> bool:
            # return True when swapping results in larger Number
            return str(a) + str(b) < str(b) + str(a)

        i = 1
        while i < len(nums):
            j = i
            while j > 0 and check_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1

            i += 1

        return str(int(''.join(map(str, nums))))

if __name__ == "__main__":
    nums = [10,2]
    print(Solution().largestNumber(nums))
'''
Need more practice with recursion
'''

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        # base case
        if (len(nums) == 1):
            return [nums[:]]
            # return [nums.copy()]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:  # perms = [[2, 3], [3, 2]]
                perm.append(n)
            result.extend(perms)
            nums.append(n)

        return result
        

if __name__ == "__main__":
    nums = [1,2,3]
    print(Solution().permute(nums))
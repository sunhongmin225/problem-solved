from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def permute_rec(nums):
            ## if nums has one component, return [[nums]]
            if len(nums) == 1:
                tmp = []
                tmp.append(nums)
                return tmp

            ans = []
            ## for all components in nums, return [i-th, permute([remaining])]
            for i, num in enumerate(nums):
                red_nums = nums[0:i] + nums[i+1:]
                sub_list = permute_rec(red_nums)
                for sub in sub_list:
                    tmp=[]
                    tmp.append(num)
                    ans.append(tmp+sub)
            return ans
        
        return permute_rec(nums)

#Solution().permute([1,2,3])
#Solution().permute([0,1])
#Solution().permute([1])
Solution().permute([-1, 1,2, 3,4])

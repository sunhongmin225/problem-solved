from typing import List
class Solution: 
    list_target = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.findTargetSub(nums, target)

    def findTargetSub(self,nums_sub, target):
        ret = 0
        if len(nums_sub) == 1:
            if nums_sub[0]==target or nums_sub[0]==-target:
                if target==0:
                    ret = 2
                else:
                    ret = 1
            else:
                ret = 0
        else:
            ret +=self.findTargetSub(nums_sub[1:], target+nums_sub[0])
            ret +=self.findTargetSub(nums_sub[1:], target-nums_sub[0]) 
        
        return ret

a = Solution().findTargetSumWays([25,18,47,13,45,29,15,45,33,19,39,15,39,45,17,21,29,43,50,10], 25)
print(a)

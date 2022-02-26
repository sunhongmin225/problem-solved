from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # when nums is only composed of "0" return 0
        if len(set(nums) - set([0])) == 0:
            return "0"
        
        count = len(nums)
        
        # make a dictionary of {MSD: list}
        MSD = {}
        for num in nums:
            msd = int(str(num)[0])
            if msd not in MSD:
                MSD[int(str(num)[0])] = []
                MSD[int(str(num)[0])].append(num)
            else:
                MSD[int(str(num)[0])].append(num)
        MSD = dict(sorted(MSD.items(), reverse=True))

        # compare two cases and return 1 if "right+left" if bigger than "left+right"
        def priority(left, right):
            sleft = str(left)
            sright = str(right)
            if int(sleft+sright) < int(sright+sleft):
                return 1
            else:
                return 0
        
        # sort based on priority func and return the maximal combination
        def max_string(value):
            niter = len(value) - 1
            while niter:
                for i in range(niter):
                    if priority(value[i], value[i+1]):
                        value[i], value[i+1] = value[i+1], value[i]
                niter -= 1
            ret = ""
            for val in value:
                ret += str(val)
            return ret
       
        # add higher MSD first, and if the len(list) > 0, then compare all the combinations
        ans = ""
        for key, value in MSD.items():
            if len(value) == 1:
                ans += str(value[0])
            else:
                ans += max_string(value)
        return ans



nums = [10,2]
nums = [3,30,34,5,9]
#nums = [1, 0, 0]
nums = [34323,3432]
Solution().largestNumber(nums)

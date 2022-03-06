import copy

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
    
        def backtrack(l):
            if len(l) == len(nums):
                res.append(copy.deepcopy(l))
                return
            
            for elem in nums:
                if elem not in l:
                    l.append(elem)
                    backtrack(l)
                    l.pop(len(l)-1)
                    
        backtrack([])
        return res

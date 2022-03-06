from typing import List

class Solution:
    def __init__(self):
        self.permutations = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # return list(permutations(nums))
        self.backtrack(nums, [])
        return self.permutations
    
    def backtrack(self, nums, permutation):
        if len(permutation) == len(nums):
            self.permutations.append(permutation)
            return
        for num in nums:
            if num in permutation:
                continue
            self.backtrack(nums, permutation+[num])


if __name__=="__main__":
	nums = [1,2,3]
	# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
	print(Solution().permute(nums))

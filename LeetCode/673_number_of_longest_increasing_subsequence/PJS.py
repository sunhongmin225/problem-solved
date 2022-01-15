# I could not solve this by myself, so I watched some youtube videos...!

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        nums_len = len(nums)
        length= [1] * nums_len  # length of seq that ends at i
        count = [1] * nums_len  # number of seq that end at i
        
        maxlen = 1
        
        for i in range(nums_len):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        # means the length will increase, and the seq will be a longer one  
                        length[i] = length[j] + 1
                        count[i] = count[j]
                    elif length[j] + 1 == length[i]:
                        # means there is another seq with the same len and ends at i
                        count[i] += count[j]
            maxlen = max(maxlen, length[i])
                
        result = 0
        for i in range(nums_len):
            if length[i] == maxlen:
                result += count[i]
        
        return result
        
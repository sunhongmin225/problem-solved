import math
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        
        # make a set that holds all numbers
        numbers = set(int(x, 2) for x in nums)
        
        for num in range(int(math.pow(2, n))):
            if num not in numbers:
                bin_num = format(num, "b")
                if len(bin_num) != n:
                    prefix = "0" * (n - len(bin_num))
                    bin_num = prefix + bin_num
                return bin_num

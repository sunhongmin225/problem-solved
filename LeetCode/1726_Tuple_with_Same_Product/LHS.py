from typing import List
import math

# Refer to https://leetcode.com/problems/tuple-with-same-product/discuss/1753465/Python3-O(N2)-solution

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        # the key of hashMap is unique product value
        # count: return value
        # final: set of products
        hashMap = {}
        count = 0
        final = set()
        
        # hashMap space complexity -> O(N^2)
        # final array space complexity  -> O(N/4) -> O(N)
        
        """
        TIME: O(N^2)
        SPACE: O(N^2)
        """
        
        # time: O(N^2)
        # Search for a (product-pair) pairs
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                first = nums[i]
                second = nums[j]
                if first * second not in hashMap:
                    hashMap[first * second] = [(first,second)]
                elif first * second in hashMap:
                    hashMap[first * second].append((first,second))
                    final.add(first*second)
        
        # O(N)
        # combine each combinations and multiply 8 for each pair
        for product in final:
            n = len(hashMap[product])
            comb = math.factorial(n)/(math.factorial(n-2)*math.factorial(2))
            count += comb * 8
        
        return int(count)

# my solution-> time limit exceed
class Solution_timelimit:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = len(nums)
        
        ans = []
        for i in range(count-1):
            for j in range(i+1, count):
                product = nums[i] * nums[j]
                # exclude i, j-th elements
                red = [val for index, val in enumerate(nums) if (index != i and index != j)]
                if len(red) >= 2:
                    for ii in range(len(red)-1):
                        for jj in range(ii+1, len(red)):
                            temp = []
                            # when nums[i]*nums[j] is same as red[ii]*red[jj]
                            if product == red[ii] * red[jj]:
                                temp.extend([nums[i], nums[j], red[ii], red[jj]])
                                ans.append(temp)
        return len(ans)*4




nums = [2,3,4,6]
nums = [1, 2, 4, 5, 10]
Solution().tupleSameProduct(nums)

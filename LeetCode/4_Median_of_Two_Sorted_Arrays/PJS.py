class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        idx1 = 0
        idx2 = 0
        merged_arr = []
        if len(nums1) == 0:
            return self.findMedian(nums2)
        elif len(nums2) == 0:
            return self.findMedian(nums1)
        
        while(True):
            # continuously add the larger number to merged_arr
            if idx1 < len(nums1):
                num1 = nums1[idx1]
            else:
                num1 = 10**6 + 1
            
            if idx2 < len(nums2):
                num2 = nums2[idx2]
            else:
                num2 = 10**6 + 1
                
            if num1 <= num2:
                merged_arr.append(num1)
                idx1 += 1
            else:
                merged_arr.append(num2)
                idx2 += 1
            
            if idx1 >= len(nums1) and idx2 >= len(nums2):
                break
            
            
        return self.findMedian(merged_arr)
    
    def findMedian(self, nums):
        middle_idx = len(nums) // 2
        
        if len(nums) % 2 == 0:
            return (nums[middle_idx] + nums[middle_idx-1]) / 2
        else:
            return nums[middle_idx]

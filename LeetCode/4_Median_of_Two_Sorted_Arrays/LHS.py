class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # define longer list to long, and shorter list to short
        if len(nums1) >= len(nums2):
            long = nums1
            short = nums2
        else:
            long = nums2
            short = nums1
        
        # binary search with while loop
        def bin_search(long, num, left, right):
            while left < right:
                mid = (left + right) // 2
                if long[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            return left
            
        # for every number in short, add to list long 
        for num in short:
            pos = bin_search(long, num, 0, len(long))
            long = long[0:pos] + [num] + long[pos:]
        
        m = len(long)
        # if total list number is even, return ( long[m/2] + long[m/2 -1 ] ) / 2
        if m % 2 == 0:
            return (float(long[m//2]) + float(long[m//2-1]))/2
        # if totla list number is odd, return long[m//2]
        else:
            return float(long[m//2])
        

# very easy way of using a double for loop --> O(mn)
# better way: sort first list + find an element of second list in sorted first list using binary-search 
# hash

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = {}
        nums2_dict = {}
        
        intersection = []
        
        for elem in nums1:
            if elem in nums1_dict:
                nums1_dict[elem] += 1
            else:
                nums1_dict[elem] = 1
        
        for elem in nums2:
            if elem in nums2_dict:
                nums2_dict[elem] += 1
            else:
                nums2_dict[elem] = 1
        
        for k in nums1_dict:
            if k in nums2_dict:
                intersection += [k] * min(nums1_dict[k], nums2_dict[k])
        
        return intersection

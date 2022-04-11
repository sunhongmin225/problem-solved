
# Reference: https://intrepidgeeks.com/tutorial/leetcode-problem-350-intersection-of-two-arrays-ii
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for k in nums1:
            # print(f"nums1: {nums1}")
            # print(f"nums2: {nums2}")
            # print(f"res: {res}")
            if k in nums2:
                res.append(k)
                nums2.remove(k)
        return res
        

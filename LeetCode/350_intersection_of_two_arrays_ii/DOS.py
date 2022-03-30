from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        intersectKeys = set(nums1) & set(nums2)
        for key in intersectKeys:
            minReps = min(Counter(nums1)[key], Counter(nums2)[key])
            for _ in range(minReps):
                result.append(key)
        return result

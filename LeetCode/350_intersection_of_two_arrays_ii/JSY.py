from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dict = dict({})
        nums2_dict = dict({})

        for num in nums1: 
            if num not in nums1_dict:
                nums1_dict[num] = 1
            else:
                nums1_dict[num] += 1
        
        for num in nums2:
            if num not in nums2_dict:
                nums2_dict[num] = 1
            else:
                nums2_dict[num] += 1
        
        nums1_key = set([key for key in nums1_dict])
        nums2_key = set([key for key in nums2_dict])

        key_in_common = nums1_key - (nums1_key - nums2_key) if len(nums1_key) > len(nums2_key) else nums2_key - (nums2_key - nums1_key)

        answer = []
        for key in key_in_common:
            freq = min(nums1_dict[key], nums2_dict[key])
            answer.extend([key]*freq)
        
        return answer


if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2))

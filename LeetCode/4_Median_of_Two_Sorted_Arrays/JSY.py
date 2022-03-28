# 1. log안에 풀라는 거 보고 binary search인 거는 알았지만 어느 시점에서 어떻게 partition 해야할 지 잘 모르겠었음. 
# 2. reference: https://www.youtube.com/watch?v=q6IEA26hvXc 

from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We will do binary search only on the shorter list. 
        # Name the shorter list to A. 
        if len(nums1) < len(nums2):
            A, B = nums1, nums2
        else:
            A, B = nums2, nums1

        # Initialize
        total = len(nums1) + len(nums2)
        half = int(total / 2)

        # Note: We will do binary search only on the shorter list. 
        # left partition of A: up to the middle index
        # left partition of B: half - the length of A's left partition
        l, r = 0, len(A) - 1
        while True:
            i = int((l + r) / 2)   # A
            j = half - i - 2       # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # 1. We've found the medium
            if Aleft <= Bright and Bleft <= Aright:
                # if the len(A) + len(B) is odd
                if total % 2:
                    return min(Aright, Bright)
                # if the len(A) + len(B) is even
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) // 2
            # 2. nums in A are too big compared to nums in B
            elif Aleft > Bright: 
                r = i - 1
            # 3. nums in A are too small compared to nums in A
            else:
                l = i + 1


if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
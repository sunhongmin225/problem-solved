# Type: DP

# Retrospect
# 1. LIS 문제를 제대로 이해하지 못한다는 걸 알게 되었다. 관련 문제를 다시 한 번 다 봐야할 듯.
# 2. range 거꾸로 할 때 실수하지 않기.
# 3. 참고했던 reference： https://www.geeksforgeeks.org/number-of-longest-increasing-subsequences/


from typing import List

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        len_of_LIS = [1] * n
        dp_count = [1] * n

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[i] <= nums[j]:
                    continue

                if len_of_LIS[j] + 1 > len_of_LIS[i]:
                    len_of_LIS[i] = len_of_LIS[j] + 1
                    dp_count[i] = dp_count[j]
                elif len_of_LIS[j] + 1 == len_of_LIS[i]:
                    dp_count[i] += dp_count[j]
        
        # the maximum element from dp_l
        max_length = max(x for x in len_of_LIS)

        count = 0

        for l, c in zip(len_of_LIS, dp_count):
            if l == max_length:
                count += c
        return count


    # def findNumberOfLIS(self, nums: List[int]) -> int:
    #     nums = [None] + nums
    #     # print(nums)
    #     length = len(nums)
    #     len_of_LIS = [1] * (length)
    #     count = [1] * (length)

    #     # fill the DP array
    #     for i in range(2, length):
    #         max_least_index = 0
    #         for j in range(i-1, 0, -1):
    #             # print(i, j)
    #             # print(nums[i], nums[j])
    #             if nums[i] > nums[j]:
    #                 max_least_index = j 
    #                 break

    #         assert max_least_index <= i

    #         if max_least_index == 0:
    #             len_of_LIS[i] = 1
    #             if len_of_LIS[i] == len_of_LIS[i - 1]:
    #                 count[i] = count[i - 1] + 1
    #             else:
    #                 count[i] = 1
    #         elif max_least_index < i:
    #             len_of_LIS[i] = len_of_LIS[max_least_index] + 1
    #             if len_of_LIS[i] == len_of_LIS[i - 1]:
    #                 count[i] = count[i - 1] + 1
    #             else:
    #                 count[i] = count[i - 1]
    #     # print(count)
    #     return count[-1]
            

if __name__ == "__main__":
    nums = [1,3,5,4,7]
    # nums = [2, 2, 2, 2, 2]
    # nums = [2, 1]
    # nums = [3, 1, 2]
    print(Solution().findNumberOfLIS(nums))
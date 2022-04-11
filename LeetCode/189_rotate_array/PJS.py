class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or k == 0:
            return
        else:
            if k > len(nums):
                k = k % len(nums)
                
            front_part = nums[:-k]
            back_part = nums[-k:]
            nums[:k] = back_part
            nums[k:] = front_part

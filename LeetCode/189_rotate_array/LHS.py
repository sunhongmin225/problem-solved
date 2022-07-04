class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
	# for the case of k >= length
        shift = k % length
 
        buf = []
        for i in range(shift):
            buf.append(nums[length - shift + i])
        nums[shift:] = nums[0:length-shift]
        for i in range(shift):
            nums[i] = buf[i]
        

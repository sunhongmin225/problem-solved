class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        num_list = []
        ## append nums in decimal format
        for binary in nums:
            num_list.append(int(binary,2))

        ## iterate 0 to 2**n-1, return the absent number
        for i in range(2**len(nums)):
            if i not in num_list:
                return(bin(i)[2:].zfill(len(nums)))

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        if (nums_len := len(nums)) == 1:
            return '0' if '1' in nums else '1'
        max_int = nums_len ** 2
        nums_int = [int(n,2) for n in nums]
        for i in range(max_int):
            if i not in nums_int:
                return format(i, 'b').zfill(nums_len)

_as = ['111', '011', '001']
print(Solution().findDifferentBinaryString(_as))

_as = ['00', '01']
print(Solution().findDifferentBinaryString(_as))

_as = ['11', '01']
print(Solution().findDifferentBinaryString(_as))

_as = ['1']
print(Solution().findDifferentBinaryString(_as))

_as = ['0']
print(Solution().findDifferentBinaryString(_as))
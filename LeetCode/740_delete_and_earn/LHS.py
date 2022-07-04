from typing import List
from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        ret_max = 0
        counter = Counter(nums)
        if len(counter)==1:
            return list(counter.keys())[0]*list(counter.values())[0]
        for num in counter:
            ret = num
            temp = {key: value for key, value in counter.items()}
            if temp[num]>=2:
                temp[num] -=1
            elif temp[num]==1:
                temp.pop(num)
            temp = {key: value for key, value in temp.items() if (key != num+1) and (key != num-1)}
            ret += self.deleteAndEarn(temp)

            if ret > ret_max:
                ret_max = ret
        
        return ret_max



a = Solution().deleteAndEarn([3, 4, 2])
print(f"ans is 6, a:{a}")
a = Solution().deleteAndEarn([2, 2, 3, 3, 3, 4])
print(f"ans is 9, a:{a}")

from typing import List
from collections import defaultdict, Counter

class Solution:
    def groupAnagrams(self, strs):
        ans = defaultdict(list)
        for s in strs:
            counts = dict(Counter(s))
            orderedCounts = sorted(counts.items())
            ans[orderedCounts.__str__()].append(s)
        return ans.values()

z = ["eat","tea","tan","ate","nat","bat"]
print(
    Solution().groupAnagrams(z)
)
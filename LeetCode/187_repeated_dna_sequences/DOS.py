# chose simplicity over efficiency
from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        subseq = [s[i:i+10] for i in range(len(s)-9)]
        return {_s for _s, _c in Counter(subseq).items() if _c > 1}


if __name__=="__main__":
    s = "AAAAAAAAAAAAA"
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT" # ["AAAAACCCCC","CCCCCAAAAA"]
    print(
        Solution().findRepeatedDnaSequences(s)
    )

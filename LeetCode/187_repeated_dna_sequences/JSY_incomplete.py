# Type: DP라고 생각했지만 Hash

# Retrospect
# DP를 사용해야한다고 생각하다가 망함. 
# Hash 자료구조를 사용하기 좋은 문제들은 어떤 특징이 있는 건지 알아야겠다. 

from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        total = set()
        ans = set()

        for i in range(10, len(s) + 1):
            seq = s[i-10:i]
            if seq in total:
                ans.add(seq)
            else:
                total.add(seq)
        return list(ans)


if __name__ == "__main__":
    # s = "AAAAAAAAAAAAA"
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

    print(Solution().findRepeatedDnaSequences(s))
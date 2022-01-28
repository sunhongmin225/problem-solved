# TYPE: 구현..?

# Retrospect
# 1. edge case를 따지기 싫었다... 그래서 bulk로 계산하는 방법을 떠올렸더니 괜찮았던 듯. 

import math
from typing import List

class Solution:
    def solve(self, N: int, words: List[str]) -> int:
        # 1. make a dictionary for each alphabet on how much weight it holds
        # eg. {'G': 100, 'C': 1010, 'F': 1, 'A': 10000, 'D': 100, 'E': 10, 'B': 1}
        lookup = dict([])
        for word in words:
            for idx, alphabet in enumerate(word):
                if alphabet in lookup:
                    lookup[alphabet] += int(math.pow(10, len(word) - idx - 1))
                else:
                    lookup[alphabet] = int(math.pow(10, len(word) - idx - 1))
        
        # 2. give higher value to the alphabet that has bigger weight
        sorted_lookup = sorted(lookup.items(), key=lambda item:item[1], reverse=True)

        NUM = 9
        ans = 0
        for key, value in sorted_lookup:
            ans += NUM * value
            NUM -= 1
        
        return ans


if __name__ == "__main__":
    N = int(input())
    words = []
    for _ in range(N):
        words.append(input())

    print(Solution().solve(N, words))

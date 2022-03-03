'''
1. Referred to this explanation: https://www.youtube.com/watch?v=Sx9NNgInc3A
2. Should work on more DP problems. 
'''

from typing import List

class Solution:
    # Reference
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]

if __name__ == "__main__":
    s = "abcd"
    wordDict = ["a", "abc", "b", "cd"] # edge case

    print(Solution().wordBreak(s, wordDict))
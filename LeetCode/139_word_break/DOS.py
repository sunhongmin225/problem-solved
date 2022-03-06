"""
divide word to smaller words
word => leftword + rightword
store bool to dp table if leftword is in worddict and rightword is in worddict
"""
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]):
        tbl = [0] * (len(s)+1)
        tbl[0] = 1 # init
        
        for i in range(1, len(s)+1):
            for j in range(i):
                is_left_in_wd = tbl[j]
                is_right_in_wd = 1 if s[j:i] in wordDict else 0
                if is_left_in_wd == is_right_in_wd == 1:
                    tbl[i] = 1
                    break
        return tbl[len(s)]

                

if __name__=="__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    print(Solution().wordBreak(s, wordDict))
    # Output: true

    s = "applepenapple"
    wordDict = ["apple","pen"]
    print(Solution().wordBreak(s, wordDict))
    # Output: true

    s = "catsandog"
    wordDict = ["cats","dog","sand","and","cat"]
    print(Solution().wordBreak(s, wordDict))
    # Output: false

    s = "cars"
    wordDict = ["car","ca","rs"]
    print(Solution().wordBreak(s, wordDict))
    # Output: true
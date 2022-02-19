from typing import List
class Solution:
   
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ## if s is [] matching is finished
        if len(s) == 0:
            return True
        ## for all words, if the first "word" is same as s, split s and iterate
        for word in wordDict:
            if s[0:len(word)] == word:
                ret = self.wordBreak(s[len(word):], wordDict)
                if ret == False:
                    continue
                return ret
        return False

#s = "applepenapple" 
#wordDict = ["apple","pen"]

s = "cars"
wordDict = ["car","ca","rs"]
print(Solution().wordBreak(s, wordDict))

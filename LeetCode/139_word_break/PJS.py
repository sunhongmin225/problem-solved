# timeout

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # can_be_segmented function gets a certain word and recursively checks 
        # if the word is valid in the dictionary, than continues searching for 
        # the next possible word
        def can_be_segmented(subs):
            if subs is None:
                return False
            
            if subs not in wordDict:
                return False
            
            # reaching here means possible
            self.total_len += len(subs)
            if self.total_len == len(s):
                return True
            
            new_s = s[self.total_len:]
            for j in range(len(new_s)+1):
                success = can_be_segmented(new_s[:j])
                if success:
                    return True
                
            self.total_len -= len(subs)
            return False
        
        self.total_len = 0
        for i in range(len(s)+1):
            success = can_be_segmented(s[:i])
            if success:
                return True
        
        return False

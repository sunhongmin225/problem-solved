class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) == 0:
            return s2 == s3
        if len(s2) == 0:
            return s1 == s3
        if s1[0] == s3[0]:
            a = self.isInterleave(s1[1:], s2, s3[1:])
            if a is True:
                return True
        if s2[0] == s3[0]:
            a = self.isInterleave(s1, s2[1:], s3[1:])
            if a is True:
                return True
            
        return False

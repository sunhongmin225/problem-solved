class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences = {}
        for i in range(len(s)-9):
            substring = s[i:i+10]
            if substring in sequences:
                sequences[substring] += 1
            else:
                # initializing with substring as key
                sequences[substring] = 1
        
        ret = []
        for key, value in sequences.items():
            if value > 1:
                ret.append(key)
        
        return ret
        
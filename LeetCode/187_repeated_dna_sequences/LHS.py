class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        ## index 0 ~ len-1
        st = 0
        end = len(s)-1

        ## total iteration number (10-unit)
        iter = len(s) - 10 + 1

        res = []
        ## using dict as hash table is much faster
        check = {}
        for i in range(iter):
            st_idx = st + i
            end_idx = st + i + 10
            if s[st_idx:end_idx] in check:
                if s[st_idx:end_idx] not in res:
                    res.append(s[st_idx:end_idx])
            else:
                check[s[st_idx:end_idx]]=1

        return res

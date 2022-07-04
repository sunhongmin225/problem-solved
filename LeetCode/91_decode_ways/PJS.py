class Solution:
    def numDecodings(self, s: str) -> int:
        str_len = len(s)
        
        def backtrack(idx, cnt):
            if idx < str_len and s[idx] == '0':
                return cnt
            if idx == str_len - 1 or idx == str_len-2:
                if (idx == str_len - 1) and (1 <= int(s[idx]) and int(s[idx]) <= 26):
                    cnt += 1
                if (idx == str_len - 2) and (1 <= int(s[idx:]) and int(s[idx:]) <= 26):
                    cnt += 1
            if idx < str_len:
                if 1 <= int(s[idx]) and int(s[idx]) <= 26:
                    cnt = backtrack(idx + 1, cnt)
                if 1 <= int(s[idx:idx+2]) and int(s[idx:idx+2]) <= 26:
                    cnt = backtrack(idx+2, cnt)
            return cnt
        
        total_cnt = backtrack(0, 0)
        return total_cnt

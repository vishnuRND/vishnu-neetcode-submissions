class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        
        if s_len != t_len:
            return False

        s_count = [0] * 26
        t_count = [0] * 26
        
        for i in range(s_len):
            s_count[ord(s[i])-ord('a')] += 1
            t_count[ord(t[i])-ord('a')] += 1
        
        return s_count == t_count
            
        
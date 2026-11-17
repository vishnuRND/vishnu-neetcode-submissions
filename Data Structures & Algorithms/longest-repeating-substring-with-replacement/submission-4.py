class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        n = len(s)
        char_count = [0] * 26
        res = 0
        while end < n:
            char_count[ord(s[end]) - ord('A')] += 1
            while (end-start+1) - max(char_count) > k:
                char_count[ord(s[start]) - ord('A')] -= 1
                start+=1
            res = max(res, (end-start+1))      
            end+=1
        return res 
            
        
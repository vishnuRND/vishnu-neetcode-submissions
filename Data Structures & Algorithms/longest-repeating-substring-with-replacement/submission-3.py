class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        end = 0
        n = len(s)
        char_count = [0] * 26
        res = 0
        while end < n:
            char_count[ord(s[end]) - ord('A')] += 1
            curr_win_len = end-start+1
            if curr_win_len - max(char_count) <= k:
                res = max(res, curr_win_len)
            else:
                char_count[ord(s[start]) - ord('A')] -= 1
                start+=1
            end+=1
        return res 
            
        
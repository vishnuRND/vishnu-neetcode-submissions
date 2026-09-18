class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        char_count_frequency = [0] * 26
        max_till_now = 0
        max_len = 0
        while r < len(s):
            diff = ord(s[r]) - ord('A')
            char_count_frequency[diff] += 1
            max_count  = max(char_count_frequency)
            while (r-l+1) - max_count > k:
                char_count_frequency[ord(s[l]) - ord('A')]-=1
                max_count  = max(char_count_frequency)
                l+=1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len
        
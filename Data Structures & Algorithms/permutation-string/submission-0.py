class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_count = [0] * 26
        for char in s1:
            s1_char_count[ord(char)-ord('a')] += 1
        r = 0
        l = 0
        s2_running_count = [0] * 26
        k = len(s1)
        while r < len(s2):
            s2_running_count[ord(s2[r])-ord('a')] += 1
            if r - l + 1 == k:
                if s1_char_count == s2_running_count:
                    return True
                s2_running_count[ord(s2[l])-ord('a')] -= 1
                l += 1
            r+=1
        return False

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            sCount[ord(s[i])-ord('a')]+=1
            sCount[ord(t[i])-ord('a')]-=1
        for val in sCount:
            if val != 0:
                return False
        return True
        
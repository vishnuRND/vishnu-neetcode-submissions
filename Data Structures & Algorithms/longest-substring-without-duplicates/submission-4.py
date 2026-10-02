class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0 
        r = 0
        hashMap = dict()
        result = 0
        while r < len(s):
            if s[r] not in hashMap:
                hashMap[s[r]] = r
            else:
                if hashMap[s[r]] >= l:
                    l = hashMap[s[r]]+1
                hashMap[s[r]] = r
            result = max(result, r - l + 1)
            r+=1
        return result

    
        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        N = len(s)
        end = N - 1
        while start < end:
            while start < N and not s[start].isalnum() :
                start+=1
            while end >= 0 and not s[end].isalnum():
                end-=1
            if start > end:
                break
            if s[start].lower() == s[end].lower():
                start += 1
                end -=1
            else:
                return False
        return True
        
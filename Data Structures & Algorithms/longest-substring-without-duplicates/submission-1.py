class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = dict()
        l ,r = 0, 1
        N = len(s)
        maxL = 0
        if N <= 1:
            return N
        visited[s[0]] = 0
        while r < N:
            if s[r] in visited:
                l = max(l,visited[s[r]]+1)
            visited[s[r]] = r
            maxL = max(maxL,r-l+1)
            print(l,r)
            r += 1
        return maxL


        
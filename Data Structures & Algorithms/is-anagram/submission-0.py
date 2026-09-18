class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charCount = defaultdict(int)
        for char in s:
            charCount[char]+=1
        for char in t:
            if char not in charCount:
                return False
            charCount[char]-=1
            if charCount[char] == 0:
                del charCount[char]
        if not charCount:
            return True
        return False
        
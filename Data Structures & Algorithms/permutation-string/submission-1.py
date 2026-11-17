class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char = [0] * 26
        s2_char = [0] * 26
        for char in s1:
            s1_char[ord(char)-ord('a')] += 1
        s1Len = len(s1)
        start = 0
        end = 0
        while end < len(s2):
            s2_char[ord(s2[end])-ord('a')] +=1
            if end-start +1 == len(s1):
                    if s1_char == s2_char:
                        return True
                    s2_char[ord(s2[start])-ord('a')] -=1
                    start+=1
            end+=1
        return False
        
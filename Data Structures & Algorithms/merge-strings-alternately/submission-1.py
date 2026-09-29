class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        len_word1 = len(word1)
        len_word2 = len(word2)
        i = 0 
        while i < min(len_word1, len_word2):
            result += (word1[i]+word2[i])
            i+=1
        if len_word1 > len_word2:
            while i < len_word1:
                result += word1[i]
                i+=1
        else:
            while i < len_word2:
                result += word2[i]
                i+=1

        return result
        
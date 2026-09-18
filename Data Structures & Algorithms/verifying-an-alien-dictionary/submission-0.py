class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charIndex = dict()
        wordLen = len(words)
        if wordLen == 1:
            return True
        for index, char in enumerate(order):
            charIndex[char] = index
        for i in range(1, wordLen):
            word1 = len(words[i-1])
            word2 = len(words[i])
            diffFound = False
            for j in range(min(word1, word2)):
                prev = words[i-1][j]
                curr = words[i][j]
                if prev!=curr:
                    if charIndex[prev] > charIndex[curr]:
                        return False
                    else:
                        diffFound = True
                        break
            if word1 > word2 and not diffFound:
                return False

        return True
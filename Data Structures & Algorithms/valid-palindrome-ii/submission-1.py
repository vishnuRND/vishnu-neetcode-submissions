class Solution:
    def validPalindrome(self, s: str) -> bool:

            def recur(s, i , j, charDeletion):
                if i >= j:
                    return True
                if s[i] == s[j]:
                    return True and recur(s, i+1, j-1,charDeletion)
                else:
                    if charDeletion == 1:
                        return False
                    return True and (recur(s, i+1, j,charDeletion+1) or recur(s, i, j-1,charDeletion+1))

            return recur(s, 0, len(s)-1, 0)

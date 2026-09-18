class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        if not strs:
            return ""
        len_s = len(strs)
        if len_s == 1:
            return strs[0]
        for string in strs:
            min_len = min(min_len, len(string))
        if min_len == 0:
            return ""
        res = ""
        for i in range(min_len):
            for j in range(1, len_s):
                if strs[j][i] != strs[j-1][i]:
                    return res
            res +=strs[0][i]
        return res
        

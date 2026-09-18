class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(str) for str in strs])
        result = ""
        for i in range(min_len):
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    return result
            else:
                result = result + strs[0][i]
        return result
        
        

        
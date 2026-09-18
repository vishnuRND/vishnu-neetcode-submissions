class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupAnagrms = defaultdict(list)
        for str1 in strs:
            word = "".join(sorted(str1))
            groupAnagrms[word].append(str1)

        result = list()
        for key in groupAnagrms.keys():
            result.append(groupAnagrms[key])
            
        return result
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for string in strs:
            group_anagrams["".join(sorted(string))].append(string)
        result = list()
        for key in group_anagrams:
            result.append(group_anagrams[key])
        
        return result
        
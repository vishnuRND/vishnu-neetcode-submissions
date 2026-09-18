class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
                groups[''.join(sorted(string))].append(string)
        result = list()
        for group in groups:
            result.append(groups[group])
        return result
        
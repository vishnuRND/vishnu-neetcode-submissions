class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagrams = defaultdict(list)
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char)- ord('a')] += 1
            group_anagrams[tuple(count)].append(string)
       
        return list(group_anagrams.values())
        
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for st in strs:
            res += str(len(st))
            res += '#'
            res += st
        return res
       


    def decode(self, s: str) -> List[str]:
        num = 0
        end = len(s)
        start = 0
        result = []
        print(s)
        while start < end:
            num = ""
            while s[start] != "#":
                num += s[start]
                start+=1
            num = int(num)
            str1 = ""
            start += 1 
            i = start
            while i < (start+num):
                str1 += s[i]
                i += 1
            start = i
            result.append(str1)
            num = 0
        return result

      


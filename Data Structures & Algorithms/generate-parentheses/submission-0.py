class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        def recur(index, sum1 , str1):
            if index == 2*n:
                if sum1 == 0 :
                    result.append(str1)
                return
            if sum1 < 0 or sum1 > n:
                return 
            recur(index+1, sum1+1, str1+"(")
            recur(index+1, sum1-1, str1+")")

        recur(0,0, "")
        return result
        
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = list()
        for index, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                  less_temp = stack.pop()
                  result[less_temp] = index-less_temp
            stack.append(index)
        return result
        
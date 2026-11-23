class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = list()
        for interval in intervals:
            if stack:
                while stack and stack[-1][1] >= interval[0]:
                    pop_ele = stack.pop()
                    interval = [min(interval[0], pop_ele[0]), max(interval[1],pop_ele[1])]
            stack.append(interval)
        return stack
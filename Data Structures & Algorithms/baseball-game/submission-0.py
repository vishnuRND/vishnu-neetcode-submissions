class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = list()
        for op in operations:
            if op == "+":
                  a = scores.pop()
                  b = scores.pop()
                  scores.append(b)
                  scores.append(a)
                  scores.append(a+b)
            elif op == "C":
                 scores.pop()
            elif op == "D":
                scores.append(2 * scores[-1])
            else:
                scores.append(int(op))

        return sum(scores)
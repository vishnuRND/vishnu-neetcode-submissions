class Solution:
    def isValid(self, s: str) -> bool:
        
        matching_opens = {
            "}": "{",
            ")": "(",
            "]":"["
        }
        stack = list()
        for char in s:
            if char in ["}",")","]"]:
                open_char = matching_opens[char]
                if not stack or stack[-1]!=open_char:
                    return False
                stack.pop()
            else:
                stack.append(char)
        
        if len(stack)!=0:
            return False
        return True
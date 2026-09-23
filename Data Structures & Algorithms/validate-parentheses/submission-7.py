from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            elif not stack:
                return False
            elif c == "]":
                if stack.pop() != '[':
                    return False
            elif c == ")":
                if stack.pop() != '(':
                    return False
            elif c == "}":
                if stack.pop() != '{':
                    return False
        
        if stack:
            return False

        return True
        
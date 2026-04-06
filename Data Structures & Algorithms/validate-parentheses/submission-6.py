class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeOpen =  { "}":"{", ")":"(", "]":"[" }

        for c in s:
            if c not in closeOpen:
                stack.append(c)
            else:
                if stack and stack[-1] == closeOpen[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False





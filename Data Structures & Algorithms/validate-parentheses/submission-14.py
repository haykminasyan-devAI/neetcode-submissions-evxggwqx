class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []

        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping.keys():
                if mapping[c] not in stack:
                    return False
                elif mapping[c] == stack[-1]:
                    stack.pop()

        return len(stack) == 0



    



        
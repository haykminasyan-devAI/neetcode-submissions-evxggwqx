class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        stack = []
        
        for c in s:
            if c in mapping.values():
                stack.append(c)
            elif c in mapping.keys():
                if not stack or mapping[c] != stack[-1]:  # ✅ fixed
                    return False
                stack.pop()
                
        return len(stack) == 0
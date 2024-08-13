class Solution:
    def isValid(self, s: str) -> bool:
        closers = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        
        stack = []
        for c in s:
            if c in closers:
                if not stack or stack.pop() != closers[c]:
                    return False
            else:
                stack.append(c)

        if not stack:
            return True
        else:
            return False

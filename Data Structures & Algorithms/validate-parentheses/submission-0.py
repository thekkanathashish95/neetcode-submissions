class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            # Checking if its an end type char
            if c in lookup:
                # If end type, checking for avail of valid start type and popping
                if stack and stack[-1]==lookup[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        # Finally if valid, stack should be empty
        return True if not stack else False
        
class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"]":"[", "}":"{", ")":"("}
        stack = []

        for c in s:
            # closing
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # mismatch
                else:
                    return False

            # must be an opening
            else:
                stack.append(c)

        return not stack

        


        
class Solution:
    def isValid(self, s: str) -> bool:
        correct = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        if len(s) < 2:
            return False
        check = ""
        
        stack = []
        for char in s:
            if char in correct:
                stack.append(char)
                print(stack)
            else:
                if not stack:
                    return False
                elif correct[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        return not stack